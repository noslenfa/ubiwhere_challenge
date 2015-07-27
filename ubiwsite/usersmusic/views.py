from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Users, Musics
from serializers import UsersSerializer, MusicsSerializer


def index_view(request):
    return render(request, 'index.html')


@api_view(['GET', 'POST'])
def users_list(request, id):
    """
    List all users, add users and list searched users
    """
    if request.method == 'GET':
        if id:
            users = Users.objects.filter(id=id)
        else:
            users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def musics_list(request, id):
    """
    List all musics, add musics and list searched musics
    """
    if request.method == 'GET':
        musics = Musics.objects.filter(title__contains=id)
        serializer = MusicsSerializer(musics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = MusicsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def users_delete(request, id):
    try:
        users = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsersSerializer(users)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
def musics_delete(request, id):
    try:
        musics = Musics.objects.get(id=id)
    except Musics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MusicsSerializer(musics)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        musics.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def favorites(request, id):
    if request.method == 'GET':
        users = Users.objects.get(id=id)
        musics = users.title.all()
        serializer = MusicsSerializer(musics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif  request.method == 'POST':
        users = Users.objects.get(id=id)
        musics = Musics.objects.get(title=request.data["title"])
        users.title.add(musics)
        return Response(status=status.HTTP_200_OK)


@api_view(['DELETE'])
def favorites_del(request, id, title):
    if request.method == 'DELETE':
        users = Users.objects.get(id=id)
        musics = Musics.objects.get(title=title)
        users.title.remove(musics)
        return Response(status=status.HTTP_200_OK)