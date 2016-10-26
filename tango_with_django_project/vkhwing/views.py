from django.template import RequestContext
from django.shortcuts import render_to_response
from datetime import datetime
from vkhwing.models import Album,Photos,ChatRoom
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
def decode_url(album_name_url):
	album_name=album_name_url.replace('_',' ')
	return album_name
def encode_url(album_name):
	album_name_url=album_name.replace(' ','_')
	return album_name_url
def index(request):
	name=request.user
	context = RequestContext(request)
	album_list = Album.objects.all()
	album_new_list=Album.objects.order_by('-date')[:5]
	context_dict={"album_new":album_new_list,"album":album_list,"name":name}
	return render_to_response('vkhwing/index.html',context_dict, context)
	
def about(request):
	context = RequestContext(request)
	return render_to_response('vkhwing/about.html', context)
def album(request,album_name_url):
	context = RequestContext(request)
	album_name = decode_url(album_name_url)
	context_dict = {'album_name': album_name,'album_name_url':album_name_url}
	try:
		album = Album.objects.get(name=album_name)
		album.count= len(Photos.objects.filter(album=album_name))
		album.save()
		photos = Photos.objects.filter(album=album).order_by('-date')
		context_dict['photos'] = photos
		context_dict['album'] = album
	except Album.DoesNotExist:
		pass
	
	return render_to_response('vkhwing/album.html', context_dict, context)

from vkhwing.forms import AlbumForm,PhotosForm,UserProfileForm
def add_album(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = AlbumForm(request.POST)
		if form.is_valid():
			album=form.save(commit=False)
			a=form.save(commit=False)
			d=encode_url(album.name)
			b='/vkhwing/album/'
			c=b+str(d)
			album.date= datetime.now()
			album.count=0
			album.save()
			return HttpResponseRedirect(c)
		else:
			print form.errors
	else:
		form = AlbumForm()
	return render_to_response('vkhwing/add_album.html', {'form': form}, context)

from vkhwing.forms import PhotosForm,UserForm
from django.forms.models import modelformset_factory
def add_photo(request, album_name_url):
	#PhotosFormSet = modelformset_factory(Photos,form=PhotosForm, extra=5)
	context = RequestContext(request)
	album_name = decode_url(album_name_url)
	if request.method == 'POST':
		#formset = PhotosFormSet(request.POST,request.FILES)
		form=PhotosForm(request.POST,request.FILES)
		if form.is_valid():
			photo=form.save(commit=False)
			photo.views=0
			photo.album=album_name
			photo.image = request.FILES['image']
			photo.date= datetime.now
			photo.user=request.user
			album = Album.objects.get(name=album_name)
			album.date = datetime.now
			album.count+=1
			a="/vkhwing/album/"
			b=album_name_url
			c=a+b
			photo.assigned= 1
			photo.save()
			album.save()
			return HttpResponseRedirect(c)			
		
		else :
			print form.errors
	else:	
		form= PhotosForm()
		#formset = PhotosFormSet()
	return render_to_response( 'vkhwing/add_photo.html',{'album_name_url': album_name_url,'album_name': album_name, 'form': form},
context)


def register(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			registered = True
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render_to_response(
		'vkhwing/register.html',
		{'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
		context)

def user_login(request):
	global name
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				name = user
				return HttpResponseRedirect('/vkhwing/')
			else:
				return HttpResponse("Your Rango account is disabled.")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.Try Again." )
	else:
		return render_to_response('vkhwing/login.html', {}, context)
from django.contrib.auth import logout
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/vkhwing/')
"""def chats(request):
	context = RequestContext(request)
	chat_rooms = ChatRoom.objects.order_by('name')[:5]
  	context_dict = {'chat_list': chat_rooms,}
  	return render_to_response('vkhwing/chats.html',context_dict, context)
from django.shortcuts import render, get_object_or_404
def chat_room(request, chat_room_id):
	context = RequestContext(request)
  	chat = get_object_or_404(ChatRoom, pk=chat_room_id)
  	return render_to_response('vkhwing/chat_room.html', {'chat': chat},context)"""
def chats_coming_soon(request):
	context = RequestContext(request)
	context_dict = {}
	return render_to_response('vkhwing/chats.html',context_dict, context)
def search(request):
	context = RequestContext(request)
	context_dict = {}
	return render_to_response('vkhwing/search.html',context_dict, context)
def profile(request):
	context = RequestContext(request)
	context_dict = {}
	return render_to_response('vkhwing/profile.html',context_dict, context)
def coming_soon(request):
	context = RequestContext(request)
	context_dict = {}
	return render_to_response('vkhwing/coming_soon.html',context_dict, context)
	




"""if formset.is_valid():
			photo = formset.save(commit=False)
			#if 'image' in request.FILES:
			for form in formset.cleaned_data:
				views=0
				title=form['title']
				album=album_name
				image = form['image']
				date= datetime.now
				user= request.user
				album = Album.objects.get(name=album_name)
				album.date = datetime.now
				album.count+=1
				a="/vkhwing/album/"
				b=album_name_url
				c=a+b
				assigned= 1
				photo = Photos(views=views,album=album,title=title,image=image,date=date,user=user,assigned=assigned)
				photo.save()
				album.save()"""
