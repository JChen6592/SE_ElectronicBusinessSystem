from .models import Taboos
from django import forms

class TabooWordEntry(forms.ModelForm):
	class Meta:
		model = Taboos
		fields = (
			'word',
		)

