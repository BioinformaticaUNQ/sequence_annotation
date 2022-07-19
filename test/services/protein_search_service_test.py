import unittest
import sys
from sequence_annotation.services.proteins_search_service import ProteinsSearchService
from test.utils.data_sample import _3lvl, _1a7e, _1ej1, _1lxa, _1thj, _2cpe, _3ogb

sys.path.append("..")


class ProteinSearchServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.service = ProteinsSearchService()

    def __basic_test_search(self, pdb_id, expected_protein_result, test_secondary_structure=False):
        response = self.service.search_in_sites(pdb_id)
        self.assertEqual(response["pdb_id"], expected_protein_result["pdb_id"])
        self.assertEqual(response["sequence"], expected_protein_result["sequence"])
        self.assertEqual(len(response["chains"]), len(expected_protein_result["chains"]))
        for i in range(len(expected_protein_result["chains"])):
            actual_response_chain = response["chains"][i]
            actual_expected_protein_result_chain = expected_protein_result["chains"][i]
            self.assertEqual(actual_response_chain["chain_id"], actual_expected_protein_result_chain["chain_id"])
            self.assertEqual(len(actual_response_chain["residues"]),
                             len(actual_expected_protein_result_chain["residues"]))
            for j in range(len(actual_expected_protein_result_chain["residues"])):
                actual_response_residue = actual_response_chain["residues"][j]
                actual_expected_protein_result_residue = actual_expected_protein_result_chain["residues"][j]
                self.assertEqual(actual_response_residue["name"], actual_expected_protein_result_residue["name"])
                self.assertEqual(actual_response_residue["number"], actual_expected_protein_result_residue["number"])
        if test_secondary_structure:
            # Empty at the moment
            self.assertEqual(len(response["secondary_structure"]), 0)
            self.assertEqual(len(expected_protein_result["secondary_structure"]), 0)
        return response

    def __basic_test_missing_residues(self, missing_testing_residues_list, missing_expected_residues_list,
                                      derive_missing_residues_list):
        self.assertEqual(len(missing_testing_residues_list), len(derive_missing_residues_list))
        self.assertEqual(len(missing_expected_residues_list), len(derive_missing_residues_list))

        for n in range(len(missing_testing_residues_list)):
            actual_missing_expected_residue = missing_expected_residues_list[n]
            actual_missing_testing_residue = missing_testing_residues_list[n]
            actual_derive_missing_residue = derive_missing_residues_list[n]

            for i in range(len(actual_missing_expected_residue)):
                derive_missing_index = actual_derive_missing_residue[i]
                actual_response_basic_p0a6b9_residue = actual_missing_testing_residue[i][derive_missing_index]
                actual_expected_basic_p0a6b9_residue = actual_missing_expected_residue[i][derive_missing_index]
                self.assertEqual(actual_response_basic_p0a6b9_residue["content_count"],
                                 actual_expected_basic_p0a6b9_residue["content_count"])
                self.assertEqual(actual_response_basic_p0a6b9_residue["content_fraction"],
                                 actual_expected_basic_p0a6b9_residue["content_fraction"])
                self.assertEqual(len(actual_response_basic_p0a6b9_residue["regions"]),
                                 len(actual_expected_basic_p0a6b9_residue["regions"]))
                try:
                    self.assertEqual(actual_response_basic_p0a6b9_residue["source_id"],
                                     actual_expected_basic_p0a6b9_residue["source_id"])
                except:
                    pass

                for j in range(len(actual_expected_basic_p0a6b9_residue["regions"])):
                    for k in range(len(actual_expected_basic_p0a6b9_residue["regions"][j])):
                        self.assertEqual(actual_response_basic_p0a6b9_residue["regions"][j][k],
                                         actual_expected_basic_p0a6b9_residue["regions"][j][k])

    def test_search_1thj(self):
        self.__basic_test_search("1thj", _1thj)

    def test_search_1a7e(self):
        self.__basic_test_search("1a7e", _1a7e)

    def test_search_1ej1(self):
        self.__basic_test_search("1ej1", _1ej1)

    def test_search_1lxa(self):
        self.__basic_test_search("1lxa", _1lxa)

    def test_search_2cpe(self):
        self.__basic_test_search("2cpe", _2cpe)

    def test_search_3lvl(self):
        response = self.__basic_test_search("3lvl", _3lvl)
        self.assertEqual(len(response["missing_residues"]), len(_3lvl["missing_residues"]))
        response_p0a6b9 = response["missing_residues"][0]["P0A6B9"]
        response_p0acd6 = response["missing_residues"][1]["P0ACD6"]
        expected_p0a6b9 = _3lvl["missing_residues"][0]["P0A6B9"]
        expected_p0acd6 = _3lvl["missing_residues"][1]["P0ACD6"]

        self.assertEqual(len(response_p0a6b9), len(expected_p0a6b9))
        self.assertEqual(len(response_p0acd6), len(expected_p0acd6))

        derive_missing_residues_p0a6b9 = ["derived-missing_residues-mobi-3lvj_A",
                                          "derived-missing_residues-mobi-3lvj_B",
                                          "derived-missing_residues-mobi-3lvk_A",
                                          "derived-missing_residues-mobi-3lvl_B",
                                          "derived-missing_residues-mobi-3lvm_A",
                                          "derived-missing_residues-mobi-3lvm_B", "derived-missing_residues-priority",
                                          "derived-missing_residues-th_90",
                                          "derived-missing_residues_context_dependent-th_90"]
        derive_missing_residues_p0acd6 = ["derived-missing_residues-mobi-3lvl_A", "derived-missing_residues-priority",
                                          "derived-missing_residues-th_90"]
        self.__basic_test_missing_residues([response_p0a6b9, response_p0acd6], [expected_p0a6b9, expected_p0acd6],
                                           [derive_missing_residues_p0a6b9, derive_missing_residues_p0acd6])

    def test_search_3ogb(self):
        self.__basic_test_search("3ogb", _3ogb)


if __name__ == '__main__':
    unittest.main()
