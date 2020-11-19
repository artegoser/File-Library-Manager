import argparse
import info
import FLIMclass

flim = FLIMclass.FLIM()

parser = argparse.ArgumentParser(description='FLIM - download files!')
families = parser.add_subparsers(title='families')

#install-----------------------------------------------------------------------------------------------------------------------------------
family_parser = families.add_parser('install', help='install file from FLIM')
family_parser.add_argument('title', nargs="+", help='filename in FLIM db')

family_parser.set_defaults(func=flim.install)

#db----------------------------------------------------------------------------------------------------------------------------------------
family_parser = families.add_parser('db', help='working with global FLIM')
db = family_parser.add_subparsers(title='db')

#db list------------------------------------------------------------------
db_parser = db.add_parser('list', help="Reads the title, name and link to a file in the global library")
db_parser.add_argument("-none")

db_parser.set_defaults(func=flim.liste)

#db info------------------------------------------------------------------
db_parser = db.add_parser('info', help="Reads the title, name and link to a file in the global library")
db_parser.add_argument("title", nargs="+", help='filename in FLIM db')

db_parser.set_defaults(func=flim.getInfo)


parser.add_argument("-v", "--version", action="count", help="version", default=0)

args = parser.parse_args()


if not vars(args):
        parser.print_usage()
else:
    if args.version >= 1:
        print("FLIM version -", info.version)
    else:
        args.func(args)