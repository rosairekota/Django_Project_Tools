from django import forms 
from django.contrib.auth.models import User


class UserForm(forms.Form):
	username=forms.CharField(label="Inserer votre nom",widget=forms.TextInput(attrs={"class":"form-control mt-3","placeholder":"Your User name"}))
	email=forms.EmailField(label="Inserer votre Email",widget=forms.EmailInput(attrs={"class":"form-control mt-3","placeholder":"Email"}))
	passeword1=forms.CharField(label="Inserer votre Mot de passe", widget=forms.PasswordInput(attrs={"class":"form-control mt-3","placeholder":"pwd"}))
	passeword2=forms.CharField(label="Confirmer votre Mot de passe",widget=forms.PasswordInput(attrs={"class":"form-control mt-3","placeholder":"pwd2"}))
	def save(self):
		User.objects.create(username=self.username, email=self.email, passeword=self.passeword)
