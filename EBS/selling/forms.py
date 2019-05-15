from django import forms
from .models import Sell, BuyFixed, BidItem

class SellItemForm(forms.ModelForm):
	class Meta:
		model = Sell
		fields = (
			'sell_type',
			'product_name',
			'product_image',
			'description',
		)

class BuyFixedForm(forms.ModelForm):
	class Meta:
		model = BuyFixed
		fields = (
			'first_name',
			'last_name',
			'address',
			'credit_card_number',
			'credit_card_expiration_date',
		)

class BidItemForm(forms.ModelForm):
	class Meta:
		model = BidItem
		fields = (
			'place_bid',
		)