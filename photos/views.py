from django.shortcuts import render, redirect
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
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        # Check Category
        if 'category' in data:
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        Photo.objects.create(
            name=data['name'], category=category,
            description=data['description'], image=image)

        return redirect('gallery')

    context = {'categories': categories}

    return render(request, 'photos/add.html', context)
