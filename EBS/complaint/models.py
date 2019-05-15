from django.db import models
from users.models import EntryForm
from django.utils import timezone

# Create your models here.
class ComplaintForm(models.Model):
	witness = models.ForeignKey(EntryForm, on_delete=models.CASCADE, related_name = "witeness")
	culprit_username = models.ForeignKey(EntryForm, on_delete=models.CASCADE, related_name = "culprit")
	info = models.TextField()
	timestamp = models.DateTimeField(default=timezone.now)