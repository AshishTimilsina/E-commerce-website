from django.shortcuts import render
from .models import Blogpost

# Create your views here.
from django.http import HttpResponse

def index(request):
    # to fetch the data from admin database in blog
    myposts=Blogpost.objects.all()
    return render(request, 'blog/index.html',{'myposts':myposts})

def blogpost(request, id):
    # to fetch the data from admin database in blogpost
    post = Blogpost.objects.filter(post_id= id)[0]
    return render(request, 'blog/blogpost.html',
                  {'post':post})