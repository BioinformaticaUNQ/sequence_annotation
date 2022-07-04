from clients.sifts_client import SiftsPDBClient
from clients.uniprot_client import UniprotPDBClient
import json

class ProteinsSearchService:

    def search(self,pdb_list, save_results):
        responses = []
        sifts_client = SiftsPDBClient()
        uniprot_client = UniprotPDBClient()
        for pdb_id in pdb_list:
            responses.append(sifts_client.summary_by_pdb_id(pdb_id))
            responses.append(sifts_client.molecules_by_pdb_id(pdb_id))
            responses.append(sifts_client.secondary_structure_by_pdb_id(pdb_id))
            responses.append(sifts_client.mappings_by_pdb_id(pdb_id))
            responses.append(uniprot_client.full_info_by_pdb_id(pdb_id))
            
        if save_results:
            output_file = open("annotations.json", "a")
            output_file.write(json.dumps(responses, indent=4, sort_keys=True))
            output_file.close()
        else:
            print(json.dumps(responses, indent=4, sort_keys=True))
