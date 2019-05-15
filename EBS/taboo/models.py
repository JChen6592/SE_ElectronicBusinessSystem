from django.db import models

class Taboos(models.Model):
	word = models.CharField(default='', max_length=100)