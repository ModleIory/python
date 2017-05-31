
# GET  

**I regard '/' as installed directory**  

### project explain  

1. **plan** is for first learn  

2. **image_deal** is for dealing my image problems

### python==3.6.1  

* after installed python , set the path of /python.exe and /Script/pip.exe into enviroment  all cmd execute statement is save in /Script
  
* the three-party libs will be installed into /Lib/site-packages , origin libs are in /Lib  

* git remember user/password : vim .git/config add ==> [credentail] helper = store  

* python import just can with module style ; All mudules are package , no path ; import a.b.c

* import top_level directory package just add '../' to sys.path like sys.path.append('../'),then , import directly  

* I wanna import something to a.py , the peer directory of a.py is in the sys.path, so ,just import as package,no need to deal them

* python import must import to a document instead of directory  ....

### Django==1.11.1  

* install Django : pip install Django==1.11.1  

* create project : django-admin.py startproject MyProjectName  

* start project : come into the root directory and python manage.py runserver 8080 [we can define its port]  

* set the templates path : find the settings.py , and set TEMPLATE = []  

* In django ，there is no > = or < , just has ifequal and if true  

* More than version python3.4 , the mysql driver use pymysql , install ==> pip install pymysql 

* Django use mysql libs default to be MySQLdb，but I use pymysql，so，I deal in __init__.py add code like 
	```
	import pymysql  
	pymysql.install_as_MySQLdb()
	```

* start a new app : python manage.py startapp TestModel

* Install app ：First:define the models.py , define fields property ; Second : In setting.py INSTALL_APPS(below list all be created in db) add TestModel which you just python manage startapp TestModel, then run below command:
	```
	1,python manage.py migrate	
	2,python manage.py makemigrations TestModel	#to test any changes happen here
	3,python manage.py migrate TestModel	
	# then discover
	1,python manage.py makemigrations # detective all apps , any changes happen . If add a name after , just test the change of this app
	2,python manage.py migrate # all apps is migrate into the mysql db . If add a name , just migrate this app
	```
	then all tebles is created ok  

* there is some strange thing , If I create an app, the model and view(controller) all in the same app directory...  

* rebuild thought:first set setting.py , and run a test , still ok , then build app ...



