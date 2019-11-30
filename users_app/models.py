from django.db import models
from django.contrib.auth.models import User 
from PIL import Image

class Profile(models.Model):

	user=models.OneToOneField(User, on_delete=models.CASCADE)
	image=models.ImageField(default='rkota.jpg', upload_to='profile_images')

	def __str__(self):
		return f'profil du user={self.user.username}'

	#On fixe la taille des images:
	def save(self):
		super().save()
		img=Image.open(self.image.path)

		if img.height>200 or img.width>200:
			output_size=(200,200)
			img.thumbnail(output_size)
			img.save(self.image.path)
