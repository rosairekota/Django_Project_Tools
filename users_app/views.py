from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .form import UserRegisterForm

def register(request):
	if request.method=='POST':
		form=UserRegisterFordecoratorsm(request.POST)
		
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'le compte de {username} a été crée avec succès!, connectez-vs')
			
			
			
			#pwd=form.cleaned_data.get('password1')
			#User.objects.create(username=username, email=email, password=f'{pwd}')
			return redirect('user-login')
	else:
		form=UserRegisterForm()
	
	
	return render(request,"users/register.html",{"form":form})

 #cette annotation permet d'imposer que l'user doit se conecter avant de voir son profile
 # Ainsi, on doit le rediriger via le file config en mettant l'url parent=login==>#LOGIN_URL='user-login'
@login_required  
def profile(request): 
	return render(request,"users/profile.html")

