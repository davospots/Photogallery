from django.shortcuts import render,redirect
from .models import Album,Photos
from django.db.models import Count
from .forms import AlbumForm,PhotoForm

# Create your views here.
def home(request):
	data=Album.objects.annotate(total_photos=Count('photos')).filter(status=True)
	return render(request, 'home.html',{'data':data})

def photos(request,album_id):
	album=Album.objects.get(id=album_id)
	data=Photos.objects.filter(album=album)
	return render(request, 'photos-list.html',{'data':data,'album':album})


def update_album(request,id):
	album=Album.objects.get(id=id)
	msg=''
	if request.method=='POST':
		form=AlbumForm(request.POST,request.FILES,instance=album)
		if form.is_valid():
			saveForm=form.save(commit=False)
			saveForm.user=request.user
			saveForm.save()
			msg='Data has been updated'
	form=AlbumForm(instance=album)
	return render(request, 'update-album.html',{'form':form,'msg':msg})

def add_album(request):
	msg=''
	if request.method=='POST':
		form=AlbumForm(request.POST,request.FILES)
		if form.is_valid():
			saveForm=form.save(commit=False)
			saveForm.user=request.user
			saveForm.save()
			msg='Data has been added'
	form=AlbumForm
	return render(request, 'add-album.html',{'form':form,'msg':msg})

def delete_album(request,id):
	Album.objects.filter(id=id).delete()
	return redirect('home')

def photo_list(request,album_id):
	album=Album.objects.get(id=album_id)
	photos=Photos.objects.filter(album=album)
	return render(request, 'photos-list.html',{'data':photos,'album':album})
	
def add_photo(request,album_id):
	album=Album.objects.get(id=album_id)
	msg=''
	if request.method=='POST':
		form=PhotoForm(request.user,request.POST,request.FILES)
		if form.is_valid():
			saveForm=form.save(commit=False)
			saveForm.save()
			msg='Data has been added'
			return redirect('/photo-list/'+str(album_id))
	form=PhotoForm(request.user)
	return render(request, 'add-photo.html',{'form':form,'msg':msg,'album':album})

def delete_photo(request,album_id,photo_id):
	Photos.objects.filter(id=photo_id).delete()
	
	return redirect('home')