from services.proteins_search_service import ProteinsSearchService
from utils.data_sample import query_data_example

protein_search_service = ProteinsSearchService()


def test_search_in_all_providers():
    response = protein_search_service.search_in_sites(query_data_example["pdb_id"])
    assert response["pdb_id"] == query_data_example["pdb_id"] \
           and response["sequence"] == query_data_example["pdb_sequence"]
