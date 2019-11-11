from django import forms


class ContactForm(forms.Form):
	fullname=forms.CharField(widget=forms.TextInput(attrs={"name":"fullname","placeholder":"name","class":"form-control"}))
	email=forms.EmailField(widget=forms.EmailInput(attrs={"name":"email" ,"placeholder":"Your Email","class":"form-control"}))
	content=forms.CharField(widget=forms.Textarea(attrs={"name":"content","placeholder":"put your text here ...","class":"form-control"}))
	
	def clean_email(self):
		email=self.cleaned_date.get("email")
		if not "gmail.com" in email: 
			raise forms.ValidationError(_("vous devez imperativement mettre le prefix @gmail.com"), code='invalid')
		return email