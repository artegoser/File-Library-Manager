import requests
from tqdm import tqdm
import json
import os
import sys
import info

class FLIM():
    def __init__(self):
        
        #self.databaseurl = info.globaldb
        self.database = self.json(info.globaldb)
        
    def install(self, args):
        for arg in args.title:
            url, name = self.getItem(arg)
            print("Downloading", name, "from", url)
            self.download(url, name)
        print("Done.")
        
    def liste(self, args):
        for arg in self.database.keys():
            url, name = self.getItem(arg)
            print("--------")
            print("Title:", arg, "\nurl:", url,"\nname:", name)
            print("--------")
            
    def getInfo(self, args):
        for arg in args.title:
            url, name = self.getItem(arg)
            print("--------")
            print("Title:", arg, "\nurl:", url,"\nname:", name)
            print("--------")
            
    def getCat(self, args):
        for arg in args.title:
            url, name = self.getItem(arg)
            print(self.cat(url))
            
    def toLocal(self, args):
        url = args.titles[0]
        name = args.titles[1]
        self.download(url, name)
        print("Done!")
        
    def ldbCreate(self, args):
        name = args.title
        with open(name, "w") as data:
            json.dump({}, data)
        print("Localdb "+name+" was created")
        
    def ldbAdd(self, args):
        
        ldbname = args.titles[0] 
        title = args.titles[1]
        name = args.titles[2]
        url = args.titles[3]
        
        new_block = {
               title:{
                   "name": name,
                   "url": url
                   }
            }
        
        with open(ldbname, "r") as data:
                localdb = json.load(data)


        localdb.update(new_block)
        with open(ldbname, "w") as data:
            json.dump(localdb, data)
        print("Block "+title+", was created")
        
    def getItem(self, title):
        if title == "packages":
            return "", ""
        return self.database[title]["url"], self.database[title]["name"]

    def download(self, url, name, savedir=""):
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

    def hidedownload(self, url, name, savedir=""):
            try:
                os.mkdir(savedir)
            except:
                pass
            r = requests.get(url, stream=True)
            block_size = 1024 
            with open(savedir + name, 'wb') as f:
                for data in r.iter_content(block_size):
                    f.write(data)

    def cat(self, url):
        return requests.get(url, stream=True).text
    def json(self, url):
        return requests.get(url, stream=True).json()