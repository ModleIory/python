
# GET  

**I regard '/' as installed directory**  

### python  

* after installed python , set the path of /python.exe and /Script/pip.exe into enviroment  all cmd execute statement is save in /Script
  
* the three-party libs will be installed into /Lib/site-packages , origin libs are in /Lib  

* git remember user/password : vim .git/config add ==> [credentail] helper = store  

* python import just can with module style ; All mudules are package , no path ; import a.b.c

* import top_level directory package just add '../' to sys.path like sys.path.append('../'),then , import directly  

*

### Django  

* install Django : pip install Django==1.11.1  

* create project : django-admin.py startproject MyProjectName  

* start project : come into the root directory and python manage.py 8080 [we can define its port]  

* set the templates path : find the settings.py , and set TEMPLATE = []




