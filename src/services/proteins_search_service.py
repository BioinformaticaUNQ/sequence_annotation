from clients.sifts_client import SiftsPDBClient
from clients.uniprot_client import UniprotPDBClient
from dto.protein import Protein
from dto.chains import Chain
from dto.residues import Residue
from dto.chains import SecondaryStructure
from dto.chains import Aminoacid
import json

class ProteinsSearchService:
    
    sifts_client = SiftsPDBClient()
    uniprot_client = UniprotPDBClient()

    def search(self,pdb_list, save_results, path):
        
        responses = []
        for pdb_id in pdb_list:
            protein = self.search_in_sites(pdb_id)
            responses.append(protein)
            
        if save_results:
            file_path = path if path else "annotations.json"
            output_file = open(file_path, "a")
            output_file.write(json.dumps(responses, indent=4, sort_keys=True))
            output_file.close()
        else:
            print(json.dumps(responses, indent=4, sort_keys=True))

    def search_in_sites(self,pdb):

        pdb_id = pdb.lower()

        #Obtains the protein sequence
        molecules = self.sifts_client.molecules_by_pdb_id(pdb_id)
        molecules_data = list(molecules[pdb_id])
        sequence = molecules_data[0].get('sequence')
        
        #Obtains the chains and its residues
        residues = self.sifts_client.residue_listing_by_pdb_id(pdb_id)
        residues_data = list(residues[pdb_id].get('molecules'))
        residues_chains = residues_data[0].get('chains')
        
        residues_response = []
        chains_and_residues = []
        for c in residues_chains:
            chain = Chain(c.get('chain_id'))
            for amins in c.get('residues'):
                r = Residue(amins.get('residue_name'), amins.get('residue_number'))
                residues_response.append(r.__dict__)
            chain.residues = residues_response
            
            foundSecondaryStruct(self,chain, pdb_id)
            
            chains_and_residues.append(chain.__dict__)
        
        
        protein = Protein(pdb_id.upper(), sequence, chains_and_residues)
        return protein.__dict__
    

def foundSecondaryStruct(self, chain, pdb_id):
    
    #Obtains wich residues are part of helices or strands
    second_struct = self.sifts_client.secondary_structure_by_pdb_id(pdb_id)
    ss_data = list(second_struct[pdb_id].get('molecules'))
    second_struct_info = ss_data[0].get('chains')
    
    helices = []
    strands = []
    structure = SecondaryStructure()

    
    for s in second_struct_info:
        if s.get('chain_id') == chain.chain_id:

            helicesFound = s.get('secondary_structure').get('helices')
            if(helicesFound):
                for h in helicesFound :
                    a = Aminoacid()
                    a.residue_number_start = h.get('start').get('residue_number')
                    a.residue_number_end = h.get('end').get('residue_number')
                    helices.append(a.__dict__)
                
            strandsFound = s.get('secondary_structure').get('strands')
            if(strandsFound):
                for p in strandsFound :
                    a = Aminoacid()
                    a.residue_number_start = p.get('start').get('residue_number')
                    a.residue_number_end = p.get('end').get('residue_number')
                    strands.append(a.__dict__)
            structure.helices = helices
            structure.strands = strands
    
    chain.secondary_structure = structure.__dict__

