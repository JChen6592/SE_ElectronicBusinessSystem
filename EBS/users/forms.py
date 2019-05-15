from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import EntryForm

class EntryUserForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = EntryForm
		fields = ('first_name', 'last_name', 'user_type', 'username')

class ProfileChange(UserChangeForm):
	class Meta:
		model = EntryForm
		fields = ('username', 'first_name', 'last_name', 'email', 'address', 'credit_card')

