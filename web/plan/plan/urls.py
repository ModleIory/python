"""plan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import pymysql

'''
	为了导入上级目录
'''
import sys

sys.path.append('../')

from . import view # import view --regard . as a package , so like that
#从上级导入的
import view_
from . import db_use
from TestModel.views import find_one

urlpatterns = [
    #操练模型
    url(r'^admin/', admin.site.urls),
    url(r'^hello$',view.hello),
    url(r'^mapi$',view_.hello),
    url(r'^show$',view.show),
    url(r'extends$',view.extends),

    #操练数据库
    url(r'insert$',db_use.save_data),
    url(r'select$',db_use.get_data),
    url(r'update$',db_use.update_data),
    url(r'delete$',db_use.delete_data),

    #把app作为模块来搞，一个app一个model加controller
    url(r'find$',find_one),
]
