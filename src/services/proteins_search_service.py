from clients.sifts_client import SiftsPDBClient
from clients.uniprot_client import UniprotPDBClient
from dto.protein import Protein
import json

class ProteinsSearchService:
    
    sifts_client = SiftsPDBClient()
    uniprot_client = UniprotPDBClient()

    def search(self,pdb_list, save_results):
        responses = []
        #sifts_client = SiftsPDBClient()
        #uniprot_client = UniprotPDBClient()
        for pdb_id in pdb_list:
            
            #responses.append(self.sifts_client.summary_by_pdb_id(pdb_id))
            #responses.append(self.sifts_client.molecules_by_pdb_id(pdb_id))
            #responses.append(self.sifts_client.secondary_structure_by_pdb_id(pdb_id))
            #responses.append(self.sifts_client.mappings_by_pdb_id(pdb_id))
            #responses.append(self.uniprot_client.full_info_by_pdb_id(pdb_id))
            
            protein = self.search_in_sites(pdb_id)
            responses.append(protein)
            
        if save_results:
            output_file = open("annotations.json", "a")
            output_file.write(json.dumps(responses, indent=4, sort_keys=True))
            output_file.close()
        else:
            print(json.dumps(responses, indent=4, sort_keys=True))
            
            
    
    def search_in_sites(self,pdb_id):

        #Obtains the protein sequence
        molecules = self.sifts_client.molecules_by_pdb_id(pdb_id)
        molecules_data = list(molecules[pdb_id])
        sequence = molecules_data[0].get('sequence')
        
        protein = Protein(pdb_id, sequence)
        return protein
