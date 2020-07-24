# Команды которые нужно сделать

## LFL 0.0.5 version - package update
### NEW commands

* package packagename install - устанавливает пакет файлов из глобальной библиотеки(библиотека внутри библиотеки)|installs a package of files from the global library (library within a library)
* package list - считывает имена всех пакетов из глобальной библиотеки|reads the names of all packages from the global library
* package packagename list - считывает все наименования, ссылки и имена файлов в пакете|
* package packagename check - проверяет пакет это или нет|
* package packagename file filename install - устанавливает файл из локальной библиотеки|

#### need this?
* ?ldb localdbname.LFL package install packagename - нужно ли? локальная библиотека сама может служить пакетом файлов|installs a package of files from the local library (library within a library)
* ?ldb localdbname.LFL create package packagename - нужно ли? создает пакет внутри локальной библиотеки|creates a package inside a local library
* ?ldb localdbname.LFL addto package packagename filetitle fileurl filename - нужно ли? добавить в пакет в локальной библиотеке файл|add file to package in local library

### Bug fixes! 

* Exception handlers
