from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . forms import movie_form

# Create your views here.
def index(request):
    movies = movie.objects.all()
    context={
        'movie_list': movies
    }
    return render(request, "index.html",context)

def details(request,movie_id):
    m=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{"m":m})

def add_movie(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        des = request.POST.get('des')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie_upload=movie(name=name,des=des,year=year,img=img)
        movie_upload.save()

    return render(request,"add.html")

def update_fn(request,id):
    movies=movie.objects.get(id=id)
    form=movie_form(request.POST or None,request.FILES, instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movies})

def delete(request,id):
    if request.method == 'POST':
        movies=movie.objects.get(id=id)
        movies.delete()
        return  redirect('/')
    return render(request,'delete.html')