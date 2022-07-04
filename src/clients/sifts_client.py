import requests
url = "https://www.ebi.ac.uk/pdbe/api/"
entry_url = url + "pdb/entry/"

class SiftsPDBClient:

    def __basic_get_call(self,base_url, domain, pdb_id):
        return requests.get(base_url + domain +"/"+ pdb_id).json()

    def summary_by_pdb_id(self, pdb_id):
        return self.__basic_get_call(entry_url,"summary",pdb_id)
    
    def molecules_by_pdb_id(self, pdb_id):
        return self.__basic_get_call(entry_url,"molecules",pdb_id)
    
    def secondary_structure_by_pdb_id(self, pdb_id):
        return self.__basic_get_call(entry_url,"secondary_structure",pdb_id)
    
    def mappings_by_pdb_id(self,pdb_id):
        return self.__basic_get_call(url,"mappings",pdb_id)
    
    def residue_listing_by_pdb_id(self,pdb_id):
        return self.__basic_get_call(entry_url,"residue_listing",pdb_id)

    