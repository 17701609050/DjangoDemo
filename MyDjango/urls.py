#coding:utf-8
"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from learn import views as learn_views  # new

urlpatterns = [
    url(r'^home/$', learn_views.index, name='home'),  # new
    url(r'^login/$', learn_views.login, name='login'),
    url(r'^user_login/', learn_views.user_login, name='user_login'),
    url(r'^project/get_chip_name/', learn_views.get_chip_name, name='get_chip_name'),
    url(r'^projects/status', learn_views.cmcc_project_gethome_project_info, name='cmcc_project_gethome_project_info'),
    url(r'^projects/all', learn_views.getproject_basic_info_by_all, name='getproject_basic_info_by_all'),
    url(r'^accounts/', include('users.urls')),
    url(r'^add/(\d+)/(\d+)/$', learn_views.old_add2_redirect), # 注意修改了这一行
    url(r'^new_add/(\d+)/(\d+)/$', learn_views.add2, name='add2'),
    url(r'^admin/', include(admin.site.urls)),
]
