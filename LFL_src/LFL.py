import requests
from tqdm import tqdm
import json
import os
import sys

def download(url, name, savedir=""):
        try:
         os.mkdir(savedir)
        except:
         pass
        r = requests.get(url, stream=True)
        total_size = int(r.headers.get('content-length', 0))
        block_size = 1024 
        t=tqdm(total=total_size, unit='B', unit_scale=True)
        with open(savedir + name, 'wb') as f:
         for data in r.iter_content(block_size):
          t.update(len(data))
          f.write(data)
        t.close()
        print("Download finished!")

def hidedownload(url, name, savedir=""):
        try:
         os.mkdir(savedir)
        except:
         pass
        r = requests.get(url, stream=True)
        total_size = int(r.headers.get('content-length', 0))
        block_size = 1024 
        with open(savedir + name, 'wb') as f:
         for data in r.iter_content(block_size):
          f.write(data)

def cat(url):
    cat = requests.get(url, stream=True)
    textcat = cat.text
    print(textcat)

databasedownload =    {
      "update": {"name": "database.LFL",
			     "url": "https://raw.githubusercontent.com/artegoser/Large-File-Library/master/Databases/database.LFL"}
    }


cd = os.getcwd()

#версия программы
version = "0.0.5"
error = 0

s = "None"
s2 = "None"
s3 = "None"
s4 = "None"
s5 = "None"
s6 = "None"
s7 = "None"
s8 = "None"
s9 = "None"
try:
    s  = sys.argv[1]
    s2 = sys.argv[2]
    s3 = sys.argv[3]
    s4 = sys.argv[4]
    s5 = sys.argv[5]
    s6 = sys.argv[6]
    s7 = sys.argv[7]
    s8 = sys.argv[8]
    s9 = sys.argv[9]
except: 
    pass

print("")

#quick commands ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if s in ["install"]: #установка файла из глобальной библиотеки
    try:
        print("I update the LFL database")
        hidedownload(url=databasedownload["update"]["url"], name=databasedownload["update"]["name"])

        with open("database.LFL", "r", encoding = "utf-8") as data:
            database = json.load(data)
        os.remove("database.LFL")
   
        print("The database has been updated.")
        try:

            print("\nDownloading: "+ s2)
            download(url=database[s2]["url"], name=database[s2]["name"])
            print("File saved in "+cd+"\\"+database[s2]["name"])

        except:
            print("There is no such File in the LFL.")
    except:
        print("The troubles with LFL global database")
    #s2=#filename
   

elif s in["version"]: #Узнать версию программы
    print("Version of Large File Library - "+ version+"\n")

#DB working with globallibrary   -------------------------------------------------------------------------------------------------------------------------------------------------------
elif s in["db"]:   #Семейство db

    try: #Обновление глобальной библиотеки
        print("I update the LFL database")
        hidedownload(url=databasedownload["update"]["url"], name=databasedownload["update"]["name"])

        with open("database.LFL", "r", encoding = "utf-8") as data:
            database = json.load(data)
        os.remove("database.LFL")
   
        print("The database has been updated.")
    except:
        print("The troubles with LFL global database")


    if s2 in["list"]: #Все названия ссылки и имена в глобальной библиотеке

            for title in database.keys():
                print("\nTitle: "+title)
                print("URL: "+database[title]["url"])
                print("Name: "+database[title]["name"]+"\n")

    elif s2 in["info"]: #узнать ссылку и имя файла в глобальной библиотеке #s3 имя файла
        try:
            print("Title: "+s3)
            print("URL: "+database[s3]["url"])
            print("Name: "+database[s3]["name"])
        except:
            print("There is no such File in the LFL.")

    elif s2 in["cat"]: #прочитать файл без скачивания в глобальной библиотеке
        try:
            cat(database[s3]["url"])
        except:
            print("There is no such File in the LFL.")

    else:
        print("There is no such command.")

#LDB working with locallibraries ------------------------------------------------------------------------------------------------------------------------------------------------
elif s in["ldb"]: #семейство ldb
            #s2 название локальной базы данных
    if s3 in["list"]: #Все названия ссылки и имена в локальной библиотеке
        try:
            with open(s2, "r", encoding = "utf-8") as data:
                localdb = json.load(data)
            print("localdb "+s2+" was read")
            for title in localdb.keys():
                print("\nTitle: "+title)
                print("URL: "+localdb[title]["url"])
                print("Name: "+localdb[title]["name"]+"\n")

        except:
            print("The "+s2+" library does not exist or it cannot be read\n")


    elif s3 in["info"]: #узнать ссылку и имя файла в локальной библиотеке #s4 имя файла
        try:
            with open(s2, "r", encoding = "utf-8") as data:
                localdb = json.load(data)
            print("localdb "+s2+" was read")
            try:
                print("Title: "+s4)
                print("URL: "+localdb[s4]["url"])
                print("Name: "+localdb[s4]["name"])
            except:
                print("There is no such File in the localdb")

        except:
            print("The "+s2+" library does not exist or it cannot be read")

    elif s3 in["install"]: #скачивание файла из локальной библиотеке
        #s4 имя файла
        try:
            with open(s2, "r", encoding = "utf-8") as data:
                localdb = json.load(data)
            print("localdb "+s2+" was read")
            try:
                print("Downloading: "+ s4)
                download(url=localdb[s4]["url"], name=localdb[s4]["name"])
                print("File saved in "+cd+"\\"+localdb[s4]["name"])
            except:
                print("There is no such File in the "+s2+" library.")
        except:
            print("The "+s2+" library does not exist or it cannot be read")
   
        
    elif s3 in["dbinstall"]: #скачивание всей локальной библиотеки

        try:
            with open(s2, "r", encoding = "utf-8") as data:
                    localdb = json.load(data)
            print("localdb "+s2+" was read")
            print("Completely starting to download the "+ s2 +" library\n")
            for title in localdb.keys():
              try:
                print("\nDownloading: "+ title)
                download(url=localdb[title]["url"], name=localdb[title]["name"])
                print("")
              except:
                  print("\nUnreadable file (wrong url or wrong syntax)")
                  print("Skipping...\n")
        except:
            print("The "+s2+" library does not exist or it cannot be read")

    elif s3 in["create"]:#Создание локальной библиотеки

        with open(s2, "w") as data:
            json.dump({}, data)
        print("Localdb "+s2+" was created")

    elif s3 in["add"]: #Добавление елементов в локальную библиотеку

        title = s4
        name = s5
        url = s6

        new_block = {
               title:{
                   "name": name,
                   "url": url
                   }
            }
        try:
            with open(s2, "r") as data:
                localdb = json.load(data)


            localdb.update(new_block)
            with open(s2, "w") as data:
                json.dump(localdb, data)
            print("Block added to library")
        except:
            print("The "+s2+" library does not exist or it cannot be read")

    elif s3 in["merge", "combine"]: #соединение локальных библиотек   #s2 первая библиотека #s4 вторая библиотека #s6 финальная библиотека

        try:
            with open(s2, "r") as data:
                   first = json.load(data)
            print(s2+" local library was read")
        except:
            print("The "+s2+" library does not exist or it cannot be read")
            error = 1

        try:
            with open(s4, "r") as data:
                   second  = json.load(data)
            print(s4+" local library was read")
        except:
            print("The "+s4+" library does not exist or it cannot be read")
            error = 1

        if error == 0:
            if s5 in["to"]:

                with open(s6, "w") as data:
                    json.dump({}, data)

                with open(s6, "r") as data:
                   final  = json.load(data)

                final.update(first)
                final.update(second)

                with open(s6, "w") as data:
                    json.dump(final, data)
                print("Libraries "+s2+" and "+s4+" successfully merged to "+s6)

            else:

                first.update(second)
                with open(s2, "w") as data:
                    json.dump(first, data)
                print("Libraries "+s2+" and "+s4+" successfully merged to "+s2)
        else:
            error = 0
            print("Can't merge libraries")


    elif s3 in["cat"]: #прочитать файл без скачивания в локальной библиотеке

        try:
            with open(s2, "r", encoding = "utf-8") as data:
                        localdb = json.load(data)
            try:
                cat(localdb[s4]["url"])
            except:
                print("There is no such File in the LFL.")
        except:
            print("The "+s2+" library does not exist or it cannot be read")


    else:
        print("There is no such command.")
    
        

else:
    print("There is no such command.")

print("")