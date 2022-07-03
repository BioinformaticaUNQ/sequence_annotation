import argparse
from services.proteins_search_service import ProteinsSearchService


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
    service = ProteinsSearchService()
    if args.pdb_ids:
        service.search(args.pdb_ids, args.save_file)
    if args.from_file:
        service.search(args.from_file, args.save_file)

if __name__ == '__main__':
    main()
