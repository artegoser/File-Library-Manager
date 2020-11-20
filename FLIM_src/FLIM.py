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
db_parser = db.add_parser('list', help="gets file names, links to them and names from the global library")
db_parser.set_defaults(func=flim.liste)

#db info------------------------------------------------------------------
db_parser = db.add_parser('info', help="reads the title, name and link to a file in the global library")
db_parser.add_argument("title", nargs="+", help='filename in FLIM db')

db_parser.set_defaults(func=flim.getInfo)

#db cat-------------------------------------------------------------------
db_parser = db.add_parser('cat', help="reading a file without downloading in the global library")
db_parser.add_argument("title", nargs="+", help='filename in FLIM db')

db_parser.set_defaults(func=flim.getCat)

#db tolocal---------------------------------------------------------------
db_parser = db.add_parser('tolocal', help="downloads the global (non-main) library to the local disk")
db_parser.add_argument("titles", nargs=2, help='1. globaldb url 2. filename')

db_parser.set_defaults(func=flim.toLocal)


#ldb---------------------------------------------------------------------------------------------------------------------------------------
family_parser = families.add_parser('ldb', help='working with local FLIM libraries')
ldb = family_parser.add_subparsers(title='ldb')

#ldb create------------------------------------------------------------------
ldb_parser = ldb.add_parser('create', help="creates a FLIM local library")
ldb_parser.add_argument("title", help='FLIM ldb filename')

ldb_parser.set_defaults(func=flim.ldbCreate)

#ldb add---------------------------------------------------------------------
ldb_parser = ldb.add_parser('add', help="adds a block to the local library")
ldb_parser.add_argument("titles", nargs=4,help='1.ldb file 2.block title 3.block filename 4.block url')

ldb_parser.set_defaults(func=flim.ldbAdd)




parser.add_argument("-v", "--version", action="version", version="FLIM version - "+info.version, help="show this version message and exit")

args = parser.parse_args()


if not vars(args):
        parser.print_usage()
else:
    args.func(args)