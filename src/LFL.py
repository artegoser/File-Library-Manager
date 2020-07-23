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




databasedownload =    {
      "update": {"name": "database.LFL",
			     "url": "https://raw.githubusercontent.com/artegoser/Large-File-Library/master/Databases/database.LFL"}
    }



cd = os.getcwd()

#версия программы
version = "0.2"


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

if s in ["install"]:
    print("I update the LFL database")
    hidedownload(url=databasedownload["update"]["url"], name=databasedownload["update"]["name"])

    with open("database.LFL", "r", encoding = "utf-8") as data:
        database = json.load(data)
    os.remove("database.LFL")
   
    print("The database has been updated.")
    #s2=#filename
    try:
        print("\nDownloading: "+ s2)
        download(url=database[s2]["url"], name=database[s2]["name"])
        print("File saved in "+cd+"\\"+database[s2]["name"]+"\n")
    except:
        print("There is no such File in the LFL.\n")

elif s in["version"]:
    print("Version of Large File Library - "+ version+"\n")

elif s in["db"]:   #Семейство db
    if s2 in["list"]:
        print("I update the LFL database")
        hidedownload(url=databasedownload["update"]["url"], name=databasedownload["update"]["name"])

        with open("database.LFL", "r", encoding = "utf-8") as data:
            database = json.load(data)
        os.remove("database.LFL")
   
        print("The database has been updated.")

        for title in database.keys():
            print("\nTitle: "+title)
            print("URL: "+database[title]["url"])
            print("Name: "+database[title]["name"]+"\n")
    else:
        print("There is no such command.")

elif s in["localdb"]: #семейство localdb
            #s2 название локальной базы данных
    if s3 in["list"]:
        try:
            with open(s2, "r", encoding = "utf-8") as data:
                localdb = json.load(data)
            print("localdb "+s2+" was read")
            for title in localdb.keys():
                print("\nTitle: "+title)
                print("URL: "+localdb[title]["url"])
                print("Name: "+localdb[title]["name"]+"\n")

        except:
            print("The "+s2+" library file does not exist or it cannot be read")
    elif s3 in["install"]:
        #s4 имя файла
        try:
            with open(s2, "r", encoding = "utf-8") as data:
                localdb = json.load(data)
            print("localdb "+s2+" was read")
            try:
                print("Downloading: "+ s4)
                download(url=localdb[s4]["url"], name=localdb[s4]["name"])
                print("File saved in "+cd+"\\"+localdb[s4]["name"]+"\n")
            except:
                print("There is no such File in the "+s2+" library.\n")
        except:
            print("The "+s2+" library file does not exist or it cannot be read")
   
        
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
            print("The "+s2+" library file does not exist or it cannot be read")

    elif s3 in["create"]:#Создание локальной библиотеки
        with open(s2, "w") as data:
            json.dump({}, data,)
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

            #localdb[title] = 
            localdb.update(new_block)
            with open(s2, "w") as data:
                json.dump(localdb, data)
            print("Block added to library")
        except:
            print("The "+s2+" library file does not exist or it cannot be read")

    else:
        print("There is no such command.")
    
        

else:
    print("There is no such command.")