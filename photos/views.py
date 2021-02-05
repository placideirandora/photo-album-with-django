from django.shortcuts import render
from .models import Category, Photo

# Create your views here.


def view_gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()

    context = {'categories': categories, 'photos': photos}

    return render(request, 'photos/gallery.html', context)


def view_photo(request, pk):
    photo = Photo.objects.get(id=pk)

    context = {'photo': photo}

    return render(request, 'photos/photo.html', context)


def add_photo(request):
    return render(request, 'photos/add.html')
