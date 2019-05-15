from django.db import models
from django.utils import timezone

# Create your models here.
applying = (
	('OU', 'Apply for Ordinary User'),
)

class OUForm(models.Model):
	subject = models.CharField("Subject", max_length = 100, choices = applying)
	first_name = models.CharField(default='', max_length=20)
	last_name = models.CharField(default='', max_length=20)
	address = models.CharField(default='', max_length=50)
	email = models.CharField(default='', max_length=50)
	date_submitted = models.DateTimeField(default=timezone.now)
	status = models.IntegerField("Status",default = 0)
	author = models.CharField("Author username", max_length = 100, unique = True)
	
