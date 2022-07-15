import unittest
import sys
sys.path.append("..")
from src.services.proteins_search_service import ProteinsSearchService
from data_sample import query_data_example

class ProteinSearchServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.service = ProteinsSearchService()

    def test_search_in_all_providers(self):
        response = self.service.search_in_sites(query_data_example["pdb_id"])
        self.assertEquals(response["pdb_id"],query_data_example["pdb_id"])
        self.assertEquals(response["sequence"],query_data_example["pdb_sequence"])

if __name__ == '__main__':
    unittest.main()