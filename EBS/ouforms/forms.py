from .models import OUForm 
from django import forms

class OUEntryForm(forms.ModelForm):
	class Meta:
		model = OUForm
		fields = ('subject', 'first_name', 'last_name', 'address', 'email') 