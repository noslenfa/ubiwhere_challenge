from models import Users, Musics
from rest_framework import serializers


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('user', 'email', 'id')


class MusicsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musics
        fields = ('title', 'artist', 'album', 'id')
