from django.db import models
from PIL import Image
from django.utils import timezone

# Create your models here.
class Sell(models.Model):
	SELLTYPE = (('Bid', 'Item for Bidding'), ('Fixed', 'Fixed Price Item'))
	product_name = models.CharField(default='', max_length=100)
	sell_type = models.CharField(choices=SELLTYPE, max_length = 100)
	product_image = models.ImageField(default='default.jpg', upload_to = 'item_pics/')
	description = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)

	def save(self,*args,**kwargs):
		super(Sell,self).save(*args,**kwargs)

		img = Image.open(self.product_image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.product_image.path)


class BuyFixed(models.Model):
	first_name = models.CharField(default='', max_length = 100)
	last_name = models.CharField(default='', max_length = 100)
	address = models.CharField(default='', max_length = 100)
	credit_card_number = models.CharField(default='', max_length = 100)
	credit_card_expiration_date = models.CharField(default='', max_length = 100)

class BidItem(models.Model):
	place_bid = models.IntegerField(default = 0)

