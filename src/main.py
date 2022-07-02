import argparse
import queries
import json


def main():
    parser = argparse.ArgumentParser(description='annotations for protein sequences and structures')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-ids', '--pdb-ids',
                       type=str,
                       nargs="*",
                       help="returns annotations for the given PDB id")
    group.add_argument('-f', '--from-file',
                       type=argparse.FileType('r'),
                       help="returns annotations for the PDB ids contained on a specified text file")
    parser.add_argument('-s', '--save-file',
                        action='store_true',
                        help="results are exported to a file")

    args = parser.parse_args()

    if args.pdb_ids:
        perform_search(args.pdb_ids, args.save_file)
    if args.from_file:
        perform_search(args.from_file, args.save_file)


def perform_search(pdb_list, save_results):
    responses = []
    for pdb_id in pdb_list:
        responses.append(queries.Queries.get_annotations(pdb_id))
    if save_results:
        output_file = open("annotations.json", "a")
        output_file.write(json.dumps(responses, indent=4, sort_keys=True))
        output_file.close()
    else:
        print(json.dumps(responses, indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
