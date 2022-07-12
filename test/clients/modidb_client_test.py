from clients.mobidb_client import MobiDBClient
from utils.data_sample import query_data_example

mobidb_client = MobiDBClient()


def test_retrieves_data_for_a_given_access_id():
    response = mobidb_client.missing_residues(query_data_example["uniprot_id"])
    assert response["acc"] == query_data_example["uniprot_id"] \
           and response["sequence"] == query_data_example["uniprot_sequence"]


