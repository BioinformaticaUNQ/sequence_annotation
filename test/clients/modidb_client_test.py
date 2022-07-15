import unittest
import sys
sys.path.append("..")
from clients.mobidb_client import MobiDBClient
from data_sample import query_data_example

class MobidbTestCase(unittest.TestCase):
    def setUp(self):
        self.client = MobiDBClient()

    def test_retrieves_data_for_a_given_access_id(self):
        response = self.client.missing_residues(query_data_example["uniprot_id"])
        self.assertEquals(response["acc"],query_data_example["uniprot_id"])
        self.assertEquals(response["sequence"],query_data_example["uniprot_sequence"])

if __name__ == '__main__':
    unittest.main()