from django.db import models

class Prices(models.Model):
	
	updatedAt = models.CharField(max_length=30)
	high = models.CharField(max_length=30)
	low = models.CharField(max_length=30)