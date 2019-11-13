from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User



posts=Post.objects.all()



def home(request):
	
	context={"posts":posts}
	return render(request,"blog/home.html",context)


def lastposts(request):
	post_p=list(filter(lambda p:p['author']=='Rosaire' or p['author']=='CoreyMs',Post.objects.all() ))
	context={"posts":post_p}
	return render(request,"blog/home.html",context)

def annonce(request):
	
	return render(request,"blog/home.html",{})
