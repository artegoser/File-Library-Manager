import argparse

parser = argparse.ArgumentParser(description='FLIM - download files!')

families = parser.add_subparsers(title='families')

family_parser = families.add_parser('install', help='install file from FLIM')
family_parser.add_argument('install', help='filename in FLIM db')


family_parser = families.add_parser('db', help='working with global FLIM')
family_parser.add_argument('db', nargs="+",help='update FLIM db')


args = parser.parse_args()
print(args)