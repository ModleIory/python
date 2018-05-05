# This is learn by myself , version is python3  
# GET  

**I regard '/' as installed directory**  

### project explain  

1. **plan** is for first learn,later I've delete it  

2. **image_deal** is for dealing my image problems ,can regard as a refer when I work

3. **reptile** is for reptile exercise with python, I find it was payed more attentions  

4. **tool** is some tools maybe I can use in the future  

5. **review** is some basic knowledge which I filled  

6. **Thread_Process** is async basic to solve some problems  

7. **Senior** is for the knowledge that I do not know

8. **arithmeticc** is for math 

9. **big_data** is for big Data research

### python==3.6.1    

* after installed python , set the path of /python.exe and /Script/pip.exe into enviroment  all cmd execute statement is save in /Script
  
* the three-party libs will be installed into /Lib/site-packages , origin libs are in /Lib  

* git remember user/password : vim .git/config add ==> [credentail] helper = store  

* python import just can with module style ; All mudules are package , no path ; import a.b.c

* import top_level directory package just add '../' to sys.path like sys.path.append('../'),then , import directly  

* I wanna import something to a.py , the peer directory of a.py is in the sys.path, so ,just import as package,no need to deal them

* python import must import to a document instead of directory  ....  

* os.path.dirname(fu) #get which directory fu is in  os.path.join(a,b) # link path a and b => os.path.isfile  os.path.isdir os.path.exist  

* Kinds of version python install in ubuntu is not difficult , because they has their own installation directory and has their own binary executable document , such like /usr/bin/python  or /usr/local/bin/python3.6 , we can execute them with directory path ; if I wanna python3 default to python3.6 instead of 3.4 , I just operate global alias  

* 

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

* scan static source with {{STATIC_URL}} how to set:
	```
		add 'django.contrib.staticfiles' in INSTALLED_APP
		add 'django.template.context_processors.static' in TEMPLATES
		set these to variables :
			STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
			STATIC_URL = '/static/'  
	```  

* during tpl extends, we can use relative path instead of package like {% extends '../base.html' %}  

* about post problems: If ajax post straightly,would show 403, because django's crfs defend;How to deal? ONE: When form [{% csrf_token %}] request to server , it will set a cookie csrf to client , TWO: Add request header "X-CSRFToken:..." ,THree: add middleware 'django.middleware.csrf.CsrfViewMiddleware', then ... it works  

* in django，what I get is not a dic or list... but a object get by model class , so use user.account instead of user['account']  

* during django model select, **filter** means where , **get** many , but get just find one!  

* reander(req,'xx.html',data) , data is dictionary , but if draw to template , do not use it like user['sex'] ,but user.sex in html page  

* In setting.py,there is a ALLOW_HOST=[],when project run online , must define which host is allow, or can not scan  

* uwsgi-- in fact , a http server of python,like apache , like phpfpm ,but like node server most ,  can run lonely , but better with nginx,but wsgi is a interface  

* run uswgi-server command :
	```
	  uwsgi --http :8003 --chdir  /usr/she/nginx/python/image_deal/ --wsgi-file /usr/share/nginx/python/image_deal/image_deal/wsgi.py  
	```
	  Also I can run with a config document :
	```
	(1)chdir=...
	(2)http=:8006
	(3)wsgi-file
	then run : uwsgi config.ini || uwsgi --ini config.ini 
	```
	how to run backstage : 
	```
	uwsgi config.ini -d logfile.log
	```  

* about port and process check:
	```
	ps -ef | grep process_name 

	netstat aunltp | grep port_num
	```  

* use nginx is just for uwsgi_pass to uwsgi server  

### Django在ubuntu上，nginx联合uwsgi的配置  

* [360doc的博文](http://www.360doc.com/content/17/0602/13/29497481_659267502.shtml)   








