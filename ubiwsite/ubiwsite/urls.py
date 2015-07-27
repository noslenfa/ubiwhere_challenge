"""ubiwsite URL Configuration

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
from usersmusic import views
from ubiwsite import settings

urlpatterns = [
    url(r'^$', views.index_view, name='index.html'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^users/(?P<id>.*)$', views.users_list, name='users_list'),
    url(r'^musics/(?P<id>.*)$', views.musics_list, name='musics_list'),
    url(r'^users_delete/(?P<id>.*)$', views.users_delete, name='users_delete'),
    url(r'^musics_delete/(?P<id>.*)$', views.musics_delete, name='musics_delete'),
    url(r'^favorites/(?P<id>.*)$', views.favorites, name='favorites'),
    url(r'^favorites_del/(?P<id>.*)/(?P<title>.*)$', views.favorites_del, name='favorites_delete'),


    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^static/(.*)/$', 'django.views.static.serve', {'document_root':settings.STATIC_URL}),

]
