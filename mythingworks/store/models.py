from django.db import models

# Create your models here.
class Product(models.Model):
	name=models.CharField(max_length=850)
	price=models.FloatField()
	description=models.TextField()
	imglink=models.CharField(max_length=800)

class Order(models.Model):
	first_name= models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	address=models.CharField(max_length=250)
	city=models.CharField(max_length=200)
	payment_method=models.CharField(max_length=200)
	payment_data=models.CharField(max_length=200)
	items=models.TextField()
	fulfilled=models.BooleanField()
