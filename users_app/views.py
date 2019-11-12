from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .form import UserForm

def register(request):
	if request.method=='POST':
		form=UserForm(request.POST)
		form.save()
		if form.is_valid():
			username=form.cleaned_data.get('username')
			return redirect(request,'blog/home.html',{})
	else:
		form=UserForm()
		context={"form":form}
	
	
	return render(request,"users/register.html",context)
