from django.db import models

class Product(models.Model):
	title=models.CharField(max_length=120)
	description=models.TextField()
	price=models.DecimalField(decimal_places=2,max_digits=20, default=30.99)

	def __str__(self):
		return f"{self.title} =${self.price}"