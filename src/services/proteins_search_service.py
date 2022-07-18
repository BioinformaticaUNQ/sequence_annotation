from requests.exceptions import HTTPError
from utils.pretty_print import PrettyPrint
from clients.sifts_client import SiftsPDBClient
from clients.uniprot_client import UniprotPDBClient
from clients.mobidb_client import MobiDBClient
from dto.protein import Protein
from dto.chains import Chain, SecondaryStructure, Aminoacid
from dto.residues import Residue
import json


class ProteinsSearchService:
    sifts_client = SiftsPDBClient()
    uniprot_client = UniprotPDBClient()
    mobidb_client = MobiDBClient()

    def search(self, pdb_list, save_results):

        responses = []
        for pdb_id in pdb_list:
            print(f"Retrieving data for {pdb_id.upper()}...")
            protein = self.search_in_sites(pdb_id)
            if protein:
                responses.append(protein)

        if responses:
            if save_results:
                file_path = save_results
                output_file = open(file_path, "a")
                output_file.write(json.dumps(responses, indent=4, sort_keys=True))
                output_file.close()
                print(f"Output file saved as {file_path}")
            else:
                PrettyPrint.ok_output("\n" + json.dumps(responses, indent=4, sort_keys=True))



    def search_in_sites(self, pdb):

        pdb_id = pdb.lower()

        # Obtains the protein pdb sequence
        try:
            molecules = self.sifts_client.molecules_by_pdb_id(pdb_id)
        except HTTPError:
            PrettyPrint.fail_output(f"ERROR: Could not find info for {pdb_id.upper()}. Verify input.")
            return

        molecules_data = list(molecules[pdb_id])
        sequence = molecules_data[0].get('pdb_sequence')

        # Obtains the chains and its residues
        residues = self.sifts_client.residue_listing_by_pdb_id(pdb_id)
        residues_data = list(residues[pdb_id].get('molecules'))
        # Take the first entity
        residues_chains = residues_data[0].get('chains')

        # Obtains the missing residues

        # pending: entries to look for:
        # mobi_th90_str_fraction
        # mobi_th50_dis_fraction
        # mobi_missing_th90_dis_fraction
        # mobi_iupl_dis_fraction
        # mobi_iups_dis_fraction

        # pending: output format:
        # { "chains": [ { "chain_id": "A", "residues": [
        # { "name": "ASP", "number": 1, “unip_seq_index”: 25, "mobi_th50_dis_fraction": true },.....}

        uniprot_summary = self.sifts_client.uniprot_data_by_pdb_id(pdb_id)
        uniprot_accession_ids = list(uniprot_summary.get(pdb_id).get("UniProt").keys())

        mobidb_annotations = []

        try:
            mobidb_annotations = [self.mobidb_client.missing_residues(accession_id) for accession_id in
                                  uniprot_accession_ids]
        except HTTPError:
            PrettyPrint.warning_output(f"WARNING: The missing residues for {pdb_id.upper()} could not be found")

        missing_residues = {}

        for annotation in mobidb_annotations:
            current_acc_data = {
                annotation.get("acc"): [dict((k, v) for k, v in annotation.items() if
                                             all(keyword in k for keyword in ["missing_residues", pdb_id]))]
            }

            for key in current_acc_data:
                for elem in current_acc_data[key]:
                    if elem:
                        current_chain_id = list(elem.keys())[0]
                        missing_residues[current_chain_id] = elem.get(current_chain_id)
                        missing_residues[current_chain_id]["uniprot_source"] = key

        residues_response = []
        chains_and_residues = []

        for c in residues_chains:
            chain = Chain(c.get('chain_id'))
            for amins in c.get('residues'):
                r = Residue(amins.get('residue_name'), amins.get('residue_number'))
                residues_response.append(r.__dict__)
            chain.residues = residues_response
            
            
            self.found_uniprot_positions(sequence, uniprot_accession_ids, chain)

            self.found_secondary_struct(chain, pdb_id)

            chains_and_residues.append(chain.__dict__)

        protein = Protein(pdb_id.upper(), sequence, chains_and_residues, missing_residues)
        return protein.__dict__

#---------------------------------------------------------------------------------------------

    def found_secondary_struct(self, chain, pdb_id):
        # Obtains which residues are part of helices or strands

        try:
            second_struct = self.sifts_client.secondary_structure_by_pdb_id(pdb_id)
        except HTTPError:
            PrettyPrint.warning_output(f"WARNING: The secondary structure for {pdb_id.upper()} could not be found")
            chain.secondary_structure = SecondaryStructure().__dict__
            return

        ss_data = list(second_struct[pdb_id].get('molecules'))
        second_struct_info = ss_data[0].get('chains')

        helices = []
        strands = []
        structure = SecondaryStructure()

        for s in second_struct_info:
            if s.get('chain_id') == chain.chain_id:

                for h in s.get('secondary_structure').get('helices'):
                    a = Aminoacid()
                    a.residue_number_start = h.get('start').get('residue_number')
                    a.residue_number_end = h.get('end').get('residue_number')
                    helices.append(a.__dict__)

                for p in s.get('secondary_structure').get('strands'):
                    a = Aminoacid()
                    a.residue_number_start = p.get('start').get('residue_number')
                    a.residue_number_end = p.get('end').get('residue_number')
                    strands.append(a.__dict__)
                structure.helices = helices
                structure.strands = strands

        chain.secondary_structure = structure.__dict__
        
    
    def found_uniprot_positions(self, sequence, uniprot_accession_ids, chain):
        
        try:
            accession_id = uniprot_accession_ids[0]
            rdata = self.sifts_client.uniprot_residues_by_accession_id(accession_id)
            uni_sequence = rdata.get(accession_id).get("sequence")
            uni_residues = rdata.get(accession_id).get("data")[0].get("residues")
            first = uni_residues[0]
            uni_sequence_sub = uni_sequence[first.get("startIndex") - 1:len(uni_sequence)]
            startPosition = sequence.index(uni_sequence_sub)
    
            i = 0
            uniprotIndex = uni_residues[0].get("startIndex")
            while i < len(chain.residues):
                if i == startPosition:
                    chain.residues[i]["uniprot_number"] = uniprotIndex
                if i > startPosition:
                    uniprotIndex = uniprotIndex + 1
                    chain.residues[i]["uniprot_number"] = uniprotIndex
                i = i + 1
        except Exception:
            PrettyPrint.warning_output(f"WARNING: The uniprot positions could not be found")

