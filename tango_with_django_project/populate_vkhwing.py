import os
def populate():
	room_no=[i for i in range (301,311)]
	print room_no 
	for j in room_no :
		add_album(j)
	for k in Album.objects.all():
		print k, "created"

def add_album(name):
	a=Album.objects.get_or_create(name=name)
	return a

# Start execution here!
if __name__ == '__main__':
	print "Starting Vk hwing population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
	from vkhwing.models import Album,Photos
	populate()
