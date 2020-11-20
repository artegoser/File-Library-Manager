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
db_parser = db.add_parser('list', help="Gets file names, links to them and names from the global library")
#db_parser.add_argument("-none")

db_parser.set_defaults(func=flim.liste)

#db info------------------------------------------------------------------
db_parser = db.add_parser('info', help="Reads the title, name and link to a file in the global library")
db_parser.add_argument("title", nargs="+", help='filename in FLIM db')

db_parser.set_defaults(func=flim.getInfo)

#db cat-------------------------------------------------------------------
db_parser = db.add_parser('cat', help="Reading a file without downloading in the global library")
db_parser.add_argument("title", nargs="+", help='filename in FLIM db')

db_parser.set_defaults(func=flim.getCat)


parser.add_argument("-v", "--version", action="version", version="FLIM version - "+info.version, help="show this version message and exit")

args = parser.parse_args()


if not vars(args):
        parser.print_usage()
else:
    args.func(args)