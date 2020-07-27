# Large-File-Library (Work on readme in progress!)
![LFL](https://raw.githubusercontent.com/artegoser/Large-File-Library/master/imgs/LFL.png "LFL")
![Status](https://img.shields.io/badge/status-working-blue?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/artegoser/Large-File-Library)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/artegoser/Large-File-Library)
![GitHub watchers](https://img.shields.io/github/watchers/artegoser/Large-File-Library)
![GitHub repo size](https://img.shields.io/github/repo-size/artegoser/Large-File-Library)
![GitHub All Releases](https://img.shields.io/github/downloads/artegoser/Large-File-Library/total)
## More About 
CLI application for reading and creating LFL 
libraries.  The standard library will be updated 
all the time.  The original library can serve as 
a repository of data about files by name, this 
provides quick access to the files you need.
LFL libraries are convenient because 
* you can 
create a whole package of files that can be 
downloaded with just one command.

-------

CLI приложение для считывания и создания LFL 
библиотек. Стандартная библиотека будет 
дополнятся все время. Оригинальная библиотека 
может служить как хранилище данных о файлах по 
имени, это обеспечивает быстрый доступ к нужным 
файлам.
LFL библиотеки удобны тем 
* что вы можете создать 
целый пакет файлов который можно будет скачать 
всего одной командой.

## Installation
[Installation guide](https://github.com/artegoser/Large-File-Library/wiki/installation "installation guide") 

## Commands for the latest version LFL (0.0.4)
	LFL - Must be added to each LFL command  (is not a separate command for LFL) 


	LFL version - Displays the version of the program  
	LFL install title-of-file - Installs a file from the global library  
	

	LFL db - Working with the global library (is not a separate command for LFL) 
	     + list - Gets file names, links to them and names from the global library  
	     + info filetitle - Reads the title, name and link to a file in the global library
	     + cat filetitle - reading a file without downloading in the global library
	

	LFL ldb localdbname.LFL - Working with local libraries  (is not a separate command for LFL) 
	                      + create - Creates a local library  
	                      + add title name url - Adds a block to the local library  
	                      + install file-title-in-local-library - installs the desired file from the local library  
	                      + dbinstall - downloads completely files from the local library  
	                      + list - gets the filenames of the linked files and names from the local library
			      + info filetitle - Reads the title, name and link to a file in the local library
		              + cat filetitle - reading a file without downloading in the local library
			      + merge(or combine) secondlocaldb.LFL to finishlocaldb.LFL(optional) - merging libraries, 
												     if you don't write "to finish 		
												     localdb.LFL" the merged library 		
												     will be written to firstlocaldb.LFL


### Help wanted! / Требуется помощь! 
> We need an English translator.  Most of the words here have been translated using google translator.  If you know Russian and English you can contribute to the project.  

> Нам нужен переводчик на английский. Большинство слов здесь переведено с помощью гугл переводчика. Если вы знаете русский и английский вы можете внести вклад в проект.
