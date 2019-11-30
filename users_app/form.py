from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile



"""  
class UserForm(forms.Form):
	username=forms.CharField(label="Inserer votre nom",widget=forms.TextInput(attrs={"class":"form-control mt-3","placeholder":"Your User name"}))
	email=forms.EmailField(label="Inserer votre Email",widget=forms.EmailInput(attrs={"class":"form-control mt-3","placeholder":"Email"}))
	passeword1=forms.CharField(label="Inserer votre Mot de passe", widget=forms.PasswordInput(attrs={"class":"form-control mt-3","placeholder":"pwd"}))
	passeword2=forms.CharField(label="Confirmer votre Mot de passe",widget=forms.PasswordInput(attrs={"class":"form-control mt-3","placeholder":"pwd2"}))
	def save(self,username,email,pwd):
		User.objects.create(username=username, email=email, password=pwd)

"""
class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()

	class Meta:
		model=User
		fields=['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()

	class Meta:
		model=User
		fields=['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model=Profile
		fields=['image']
