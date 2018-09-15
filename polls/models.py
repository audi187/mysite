from django.db import models

# Create your models here.
class Persom(models.Model):
	username=models.CharField(max_length=30)
	message=models.CharField(max_length=30)



