# Large-File-Library (Work on readme in progress!)
![FLIM](https://raw.githubusercontent.com/artegoser/Large-File-Library/master/imgs/LFL.png "FLIM")
![Status](https://img.shields.io/badge/status-working-red?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/artegoser/Large-File-Library)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/artegoser/Large-File-Library)
![GitHub watchers](https://img.shields.io/github/watchers/artegoser/Large-File-Library)
![GitHub repo size](https://img.shields.io/github/repo-size/artegoser/Large-File-Library)
![GitHub All Releases](https://img.shields.io/github/downloads/artegoser/Large-File-Library/total)
## More About 
CLI application for reading and creating FLIM 
libraries.  The standard library will be updated 
all the time.  The original library can serve as 
a repository of data about files by name, this 
provides quick access to the files you need.
FLIM libraries are convenient because 
* you can 
create a whole package of files that can be 
downloaded with just one command.

-------

CLI приложение для считывания и создания FLIM 
библиотек. Стандартная библиотека будет 
дополнятся все время. Оригинальная библиотека 
может служить как хранилище данных о файлах по 
имени, это обеспечивает быстрый доступ к нужным 
файлам.
FLIM библиотеки удобны тем 
* что вы можете создать 
целый пакет файлов который можно будет скачать 
всего одной командой.

## Installation
[Installation guide](https://github.com/artegoser/File-Library-Manager/wiki/docs-installation "installation guide") 

## Commands for the latest version FLIM (0.0.4)
	FLIM - Must be added to each FLIM command  (is not a separate command for FLIM) 


	FLIM version - Displays the version of the program  
	FLIM install title-of-file - Installs a file from the global library  
	

	FLIM db - Working with the global library (is not a separate command for FLIM) 
	     + list - Gets file names, links to them and names from the global library  
	     + info filetitle - Reads the title, name and link to a file in the global library
	     + cat filetitle - reading a file without downloading in the global library
	

	FLIM ldb localdbname.FLIM - Working with local libraries  (is not a separate command for FLIM) 
	                      + create - Creates a local library  
	                      + add title name url - Adds a block to the local library  
	                      + install file-title-in-local-library - installs the desired file from the local library  
	                      + dbinstall - downloads completely files from the local library  
	                      + list - gets the filenames of the linked files and names from the local library
			      + info filetitle - Reads the title, name and link to a file in the local library
		              + cat filetitle - reading a file without downloading in the local library
			      + merge(or combine) secondlocaldb.FLIM to finishlocaldb.FLIM(optional) - merging libraries, 
												     if you don't write "to finish 		
												     localdb.FLIM" the merged library 		
												     will be written to firstlocaldb.FLIM


### Help wanted! / Требуется помощь! 
> We need an English translator.  Most of the words here have been translated using google translator.  If you know Russian and English you can contribute to the project.  

> Нам нужен переводчик на английский. Большинство слов здесь переведено с помощью гугл переводчика. Если вы знаете русский и английский вы можете внести вклад в проект.
