from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
	if request.method=='POST':
		form=UserRegisterForm(request.POST)
		
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
	if request.method=="POST":
		user_form=UserUpdateForm(request.POST,instance=request.user)
		profile_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request,f'le compte a été mise à jour avec succès!')
			
			
			
			#pwd=form.cleaned_data.get('password1')
			#User.objects.create(username=username, email=email, password=f'{pwd}')
			return redirect('user-profile')
	else:
		user_form=UserUpdateForm(instance=request.user)
		profile_form=ProfileUpdateForm(instance=request.user.profile)
	
	
	context={
		"user_form":user_form,
		"profile_form":profile_form
	}
	return render(request,"users/profile.html", context)

