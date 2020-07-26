# Команды которые нужно сделать

## LFL 0.0.5 version - big package update
### NEW commands

#### package

* package packagename install - устанавливает пакет файлов из глобальной библиотеки(библиотека внутри библиотеки)|**installs a package of files from the global library (library within a library)**
* packages list - считывает имена всех пакетов из глобальной библиотеки|**reads the names of all packages from the global library**
* package packagename list - считывает все наименования, ссылки и имена файлов в пакете|**reads all titles, urls and filenames in a package**
* package packagename check - проверяет пакет это или нет|**checks the package or not**
* package packagename file filename install - устанавливает файл из пакета|**installs a file from a package**

#### db

* db globaldburl install filename - устанавливает из глобальной(не главной) библиотеки файл|**installs a file from the global (not main) library**
* db globaldburl to local - скачивает глобальную(не главную) библиотеку на локальный диск|**downloads the global (non-main) library to the local disk**

#### ldb

* ldb localdbname.LFL package packagename install - устанавливает пакет файлов из локальной библиотеки(библиотека внутри библиотеки)|**installs a package of files from the local library (library within a library)**
* ldb localdbname.LFL packages list - считывает имена всех пакетов из локальной библиотеки|**reads the names of all packages from the local library**
* ldb localdbname.LFL package packagename list - считывает все наименования, ссылки и имена файлов в пакете|**reads all titles, urls and filenames in a package**
* ldb localdbname.LFL package packagename check - проверяет пакет это или нет|**checks the package or not**
* ldb localdbname.LFL package packagename file filename install - устанавливает файл из пакета|**installs a file from a package**
* ldb localdbname.LFL add package packagename - добавляет пакет внутри локальной библиотеки|**adds a package inside a local library**
* ldb localdbname.LFL addto package packagename filetitle filename fileurl - добавить в пакет в локальной библиотеке файл|**add file to package in local library**
* ldb localdbname.LFL packages list - считывает имена всех пакетов из локальной библиотеки|**reads the names of all packages from the local library

### Code fixes! 

* Exception handlers
* Optimizing
* More comments !!!
