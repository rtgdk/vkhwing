from django.db import models
from django.contrib.auth.models import User
import os
from datetime import datetime
def content_album_name(instance, filename):
	filename=str(instance.user) + "_" + filename
	return os.path.join(instance.album,filename)
class Album(models.Model):
	name = models.CharField(max_length=64, unique=True)
	date = models.DateTimeField(auto_now=True)
	count= models.IntegerField(default=0)
	def __unicode__(self):
		return self.name
class Photos(models.Model):
	"""album = models.ForeignKey(Album)"""
	album = models.CharField(max_length=128)
	title = models.CharField(max_length=128)
	image = models.ImageField(upload_to= content_album_name,blank=True)
	views = models.IntegerField(default=0)
	date = models.DateTimeField(auto_now=True)
	user = models.CharField(max_length=128,blank=False)
	assigned = models.IntegerField(default=0)
	def __unicode__(self):
		return self.title
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images',blank=True)
	def __unicode__(self):
		return self.user.username
from django.db import models
 
class ChatRoom(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
    	return self.name 


