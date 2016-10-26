from django.conf.urls import patterns, url
from vkhwing import views
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/',views.about, name='about'),
	url(r'^album/(?P<album_name_url>\w+)/$', views.album, name='album'),
	url(r'^add_album/$', views.add_album, name='add_album'),
	url(r'^album/(?P<album_name_url>\w+)/add_photo/$', views.add_photo, name='add_photo'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^chats/$', views.chats_coming_soon, name='chats_coming_soon'),
	url(r'^search/$', views.search, name='search'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^coming_soon/$', views.coming_soon, name='coming_soon'),)
	#url(r'^chats/$', views.chats, name='chats'),
	#url(r'^chats/(?P<chat_room_id>\d+)/$', views.chat_room, name='chat_room'))
