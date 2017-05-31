"""image_deal URL Configuration

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
from . import test_view
#为了防止命名空间冲突
# from user.views import *
import user.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/',test_view.test),

    #user
    url(r'^login$',user.views.login),
    url(r'^register$',user.views.register),
    url(r'^save_user$',user.views.save_user),
]
