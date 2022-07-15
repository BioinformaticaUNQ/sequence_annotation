import unittest
import sys

sys.path.append("..")
from src.clients.mobidb_client import MobiDBClient
from test.utils.data_sample import query_data_example


class MobidbTestCase(unittest.TestCase):
    def setUp(self):
        self.client = MobiDBClient()

    def test_retrieves_data_for_a_given_access_id(self):
        response = self.client.missing_residues(query_data_example["uniprot_id"])
        self.assertEqual(response["acc"], query_data_example["uniprot_id"])
        self.assertEqual(response["sequence"], query_data_example["uniprot_sequence"])


if __name__ == '__main__':
    unittest.main()
