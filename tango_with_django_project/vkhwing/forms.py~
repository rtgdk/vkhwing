from django import forms
from vkhwing.models import Album,Photos,UserProfile
from django.contrib.auth.models import User
class AlbumForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Please enter the album name.")
	date = forms.DateTimeField(widget=forms.HiddenInput(),required=False)
	class Meta:
		model = Album
		fields=('name','date')
class PhotosForm(forms.ModelForm):
	"""album = forms.CharField(Album,widget=forms.HiddenInput())
	title = forms.CharField(max_length=128,help_text="Please enter a title.")
	image = forms.ImageField(max_length=1000000,help_text="Please insert a photo.")
	views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	date  = forms.DateTimeField(widget=forms.HiddenInput(),required=False)
	user  = forms.CharField(widget=forms.HiddenInput(),max_length=128,required=False)"""
	class Meta:
		model = Photos
		fields = ('title', 'image')#, 'views','user')
	

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture',)
