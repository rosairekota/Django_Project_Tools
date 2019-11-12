from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User



posts=Post.objects.all()
#user=User.objects.get(pk=1)
#user.post_set.create(title="toto4",content="blabla")


def home(request):
	
	context={"posts":posts}
	return render(request,"blog/home.html",context)


def lastposts(request):
	post_p=list(filter(lambda p:p['author']=='Rosaire' or p['author']=='CoreyMs',Post.objects.all() ))
	context={"posts":post_p}
	return render(request,"blog/home.html",context)

def annonce(request):
	
	return render(request,"blog/home.html",{})
