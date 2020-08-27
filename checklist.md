# Команды которые нужно сделать

## FLIM 0.0.5 version - package update
### NEW commands

#### package

> * package packagename install - устанавливает пакет файлов из глобальной библиотеки(библиотека внутри библиотеки)|**installs a package of files from the global library (library within a library)**
> * packages list - считывает имена всех пакетов из глобальной библиотеки|**reads the names of all packages from the global library**
> * package packagename list - считывает все наименования, ссылки и имена файлов в пакете|**reads all titles, urls and filenames in a package**

#### db

> * db globaldburl install filetitle - устанавливает из глобальной(не главной) библиотеки файл|**installs a file from the global (not main) library**
> * db globaldburl to ldbname.FLIM - скачивает глобальную(не главную) библиотеку на локальный диск|**downloads the global (non-main) library to the local disk**

#### ldb


```
cancelled
* ldb localdbname.FLIM package packagename install - устанавливает пакет файлов из локальной библиотеки(библиотека внутри библиотеки)|**installs a package of files from the local library (library within a library)**
* ldb localdbname.FLIM packages list - считывает имена всех пакетов из локальной библиотеки|**reads the names of all packages from the local library**
* ldb localdbname.FLIM package packagename list - считывает все наименования, ссылки и имена файлов в пакете|**reads all titles, urls and filenames in a package**
* ldb localdbname.FLIM add package packagename - добавляет пакет внутри локальной библиотеки|**adds a package inside a local library**
* ldb localdbname.FLIM addto package packagename filetitle filename fileurl - добавить в пакет в локальной библиотеке файл|**add file to package in local library**
* ldb localdbname.FLIM packages list - считывает имена всех пакетов из локальной библиотеки|**reads the names of all packages from the local library
```

### Code fixes! 

> * Exception handlers
> * Optimizing
> * More comments !!!
