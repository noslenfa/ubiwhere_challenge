"""clientum URL Configuration

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
from django.conf.urls import include, url, patterns
from django.contrib import admin
from musics import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^users/(?P<id>.*)$', views.list_users),
    url(r'^musics/(?P<id>.*)$', views.list_musics),
    url(r'^add_user/', views.add_user),
    url(r'^add_music/', views.add_music),
    url(r'^delete_music/(?P<id>.*)$', views.delete_music),
    url(r'^delete_user/(?P<id>.*)$', views.delete_user),
    url(r'^favorites_delete/(?P<id>.*)/(?P<title>.*)$', views.favorites_delete),
    url(r'^favorites_add/(?P<id>.*)/(?P<title>.*)$', views.favorites_add),
    url(r'^tracks/', views.tracks),
    url(r'^add_tracks/(?P<title>.*)/(?P<artist>.*)/(?P<album>.*)$', views.add_tracks),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
]