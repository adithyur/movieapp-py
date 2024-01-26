from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.http import HttpResponse

def index(request):
    movie_list = Movie.objects.all()
    context = {
        'movie_list': movie_list
    }
    return render(request, "index.html", context)

def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request, "details.html",{'movie':movie})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        dis=request.POST.get('dis',)
        yr=request.POST.get('yr',)
        img=request.FILES['img']
        movie=Movie(name=name,dis=dis,yr=yr,img=img)
        movie.save()
    return render(request, "add.html")

def update(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "update.html",{'form':form,'movie':movie})

def delete(request, movie_id):
    if request.method=='POST':
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect('/')
    return render(request, "delete.html")
    
