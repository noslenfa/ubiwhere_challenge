from django import forms


class UsersForm(forms.Form):
    user = forms.CharField(label='User', widget=forms.TextInput(attrs={'placeholder': 'insert user name'}), max_length=50)
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'insert email'}), max_length=50)


class MusicsForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder': 'insert title'}), max_length=100)
    artist = forms.CharField(label='Artist', widget=forms.TextInput(attrs={'placeholder': 'insert artist name'}), max_length=100)
    album = forms.CharField(label='Album', widget=forms.TextInput(attrs={'placeholder': 'insert album name'}), max_length=100)


class MusicSearchForm(forms.Form):
    musics = forms.CharField(label='Musics to Search', widget=forms.TextInput(attrs={'placeholder': 'search music'}), max_length=100)