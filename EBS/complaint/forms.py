from .models import ComplaintForm
from django import forms

class ProcessComplaint(forms.ModelForm):
	class Meta:
		model = ComplaintForm
		fields = (
			'culprit_username',
			'info',
		)