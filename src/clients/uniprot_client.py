import requests

url = "https://rest.uniprot.org/uniprotkb/search?size=1&query="


class UniprotPDBClient:

    def full_info_by_pdb_id(self, pdb_id):
        return requests.get(url + pdb_id).json()
