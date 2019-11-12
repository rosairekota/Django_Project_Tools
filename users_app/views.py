from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .form import UserForm

def register(request):
	if request.method=='POST':
		form=UserForm(request.POST)
		
		if form.is_valid():
			username=form.cleaned_data.get('username')
			email=form.cleaned_data.get('email')
			pwd=form.cleaned_data.get('password1')
			User.objects.create(username=username, email=email, password='097054@kota')
			#return redirect(request,'users/register.html',{})
	else:
		form=UserForm()
		context={"form":form}
	
	
	return render(request,"users/register.html",context)
