from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
#list automatique
from django.views.generic import (
	ListView,
	DetailView,
	)



posts=Post.objects.all()



def home(request):
	
	context={"posts":posts}
	return render(request,"blog/home.html",context)

class PostListView(ListView):
	model=Post
	template_name="blog/home.html"  #<app>/<model>_<type_view>.html
	context_object_name='posts' 
	ordering=['-date_posted']

class PostDetailView(DetailView):
	model=Post
	template_name="blog/post_detail.html"  #<app>/<model>_<type_view>.html
	context_object_name='object'
	

def lastposts(request):
	post_p=list(filter(lambda p:p['author']=='Rosaire' or p['author']=='CoreyMs',Post.objects.all() ))
	context={"posts":post_p}
	return render(request,"blog/home.html",context)

def annonce(request):
	
	return render(request,"blog/home.html",{})
