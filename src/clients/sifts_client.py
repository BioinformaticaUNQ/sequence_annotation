import requests

ebiurl = "https://www.ebi.ac.uk/pdbe/"
url = ebiurl + "api/"
entry_url = url + "pdb/entry/"
pdb_to_uniprot_mapping_url = "mappings/uniprot/"
residues_uniprot_url = "graph-api/uniprot/interface_residues/"


class SiftsPDBClient:

    def __basic_get_call(self, base_url, domain, pdb_id):
        response = requests.get(base_url + domain + "/" + pdb_id)
        response.raise_for_status()
        return response.json()

    def summary_by_pdb_id(self, pdb_id):
        return self.__basic_get_call(entry_url, "summary", pdb_id)

    def molecules_by_pdb_id(self, pdb_id):
        return self.__basic_get_call(entry_url, "molecules", pdb_id)

    def secondary_structure_by_pdb_id(self, pdb_id):
        return self.__basic_get_call(entry_url, "secondary_structure", pdb_id)

    def mappings_by_pdb_id(self, pdb_id):
        return self.__basic_get_call(url, "mappings", pdb_id)

    def residue_listing_by_pdb_id(self, pdb_id):
        return self.__basic_get_call(entry_url, "residue_listing", pdb_id)

    def uniprot_data_by_pdb_id(self, pdb_id):
        return self .__basic_get_call(url, pdb_to_uniprot_mapping_url, pdb_id)
    
    def uniprot_residues_by_accession_id(self, accession_id):
        return self .__basic_get_call(ebiurl, residues_uniprot_url, accession_id)
