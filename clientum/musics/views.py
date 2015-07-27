from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UsersForm, MusicsForm, MusicSearchForm
from django.conf import settings
from django.contrib import messages

import requests


def index(request):
    return render(request, 'index.html')


def list_users(request, id):
    if id:
        r = requests.get(settings.SITE_URL +'users/' + id)
        result = r.json()
        if request.method == 'POST':
            form = MusicSearchForm(request.POST)

            if form.is_valid():
                rm = requests.get(settings.SITE_URL +'musics/'+request.POST['musics'])
                resultm = rm.json()
                return render(request, 'list_users.html', {'result' : result, 'form' : form, 'id' : id, 'musics_list' : resultm, 'favorites' : favorites_list(request, id)})
        else:
            form = MusicSearchForm()
        return render(request, 'list_users.html', {'result' : result, 'id' : id, 'form' : form, 'favorites' : favorites_list(request, id)})
    else:
        r = requests.get(settings.SITE_URL +'users/')
        result = r.json()
        return render(request, 'list_users.html', {'result' : result})


def list_musics(request, id):
    if id:
        r = requests.get(settings.SITE_URL +'musics/' + id)
    else:
        r = requests.get(settings.SITE_URL +'musics/')
    result = r.json()
    return render(request, 'list_musics.html', {'result' : result})


def add_user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UsersForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = form.cleaned_data['user']
            email = form.cleaned_data['email']
            payload = {'user': user, 'email': email}
            requests.post("https://frozen-castle-7671.herokuapp.com/users/", data=payload)
            messages.success(request, 'Added user to database!')
            return HttpResponseRedirect('/users/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UsersForm()

    return render(request, 'add_user.html', {'form': form})


def add_music(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MusicsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            title = form.cleaned_data['title']
            artist = form.cleaned_data['artist']
            album = form.cleaned_data['album']
            payload = {'title': title, 'artist': artist, 'album' : album}
            requests.post(settings.SITE_URL +'musics/', data=payload)
            messages.success(request, 'Added music to database!')
            return HttpResponseRedirect('/musics/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MusicsForm()

    return render(request, 'add_music.html', {'form': form})


def delete_music(request, id):
    requests.delete(settings.SITE_URL +'musics_delete/' + id)
    messages.warning(request, 'Music deleted from database!')
    return HttpResponseRedirect('/musics/')


def delete_user(request, id):
    requests.delete(settings.SITE_URL +'users_delete/' + id)
    messages.warning(request, 'User deleted from database!')
    return HttpResponseRedirect('/users/')


def favorites_list(request, id):
    r = requests.get(settings.SITE_URL +'favorites/' + id)
    favorites = r.json()
    return favorites


def favorites_add(request, id, title):
    payload = {'title' : title}
    requests.post(settings.SITE_URL +'favorites/' + id, data=payload)
    messages.success(request, 'Added favorite music to user!')
    return HttpResponseRedirect('/users/' + id)


def favorites_delete(request, id, title):
    requests.delete(settings.SITE_URL +'favorites_del/' + id + '/' + title)
    messages.warning(request, 'Deleted favorite music from user!')
    return HttpResponseRedirect('/users/' + id)


def tracks(request):
    r = requests.get('http://freemusicarchive.org/recent.json')
    result = r.json()
    resulttracks = result['aTracks']
    alltracks = []
    for i in resulttracks:
        alltracks.append({"title": i['track_title'], "album": i['album_title'], "artist": i['artist_name']})
    messages.success(request, 'External tracks list imported!')
    return render(request, 'tracks.html', {"atracks": alltracks})


def add_tracks(request, title, artist, album):
    payload = {'title': title, 'artist': artist, 'album' : album}
    requests.post(settings.SITE_URL +'musics/', data=payload)
    messages.success(request, 'Track added successfully to database!')
    return HttpResponseRedirect('/tracks/')