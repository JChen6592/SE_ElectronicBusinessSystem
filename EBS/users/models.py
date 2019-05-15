from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class EntryForm(AbstractUser):
	USERS = ((0, 'Guest User'),(1, 'Ordinary User'),(2, 'Super User'))
	user_type = models.IntegerField(choices= USERS, default = 0)
	first_name = models.CharField(default = '', max_length = 20)
	last_name = models.CharField(default = '', max_length = 20)
	username = models.CharField(default = '', max_length = 30, unique = True)
	address = models.CharField(default = '', max_length = 100)
	email = models.CharField(default = '', max_length = 100)
	credit_card = models.CharField(default = '', max_length = 100)
	was_denied = models.BooleanField(default = False)

	
