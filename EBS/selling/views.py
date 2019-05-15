from django.shortcuts import render, redirect, HttpResponse 
from .forms import SellItemForm, BuyFixedForm, BidItemForm
from .models import Sell 
from django.urls import reverse 

def sell_post(request):
	if request.method == "POST":
		form = SellItemForm(request.POST, request.FILES)
		if form.is_valid():
			s_form = form.save(commit=False)
			s_form.save()
			return redirect('home')
	else:
		form = SellItemForm()
	return render(request, 'sell_item_post.html', {'form': form})

def test(request):
	num_posts = Sell.objects.all()
	return render(request, 'view_sales.html', {'num_posts' : num_posts})

#search bar
def search(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	if q:
		products = Sell.objects.filter(product_name__icontains = q)
		context = {'query':q, 'products': products}
		template = 'details.html'   # if the product is found go to detail
	else:
		template =  'home.html'
		context ={}

	return render(request,template, context)

def cart(request):
#	if request.method == "GET":
	if request.method == "POST":
		form = BuyFixedForm(request.POST)
		if form.is_valid():
			bf_form = form.save(commit=False)
			bf_form.save()
			return redirect('home')
	else:
		form = BuyFixedForm()
	return render(request,'add_to_cart.html', {'form': form})

def bid_item(request):
#	if request.method == "GET":
	if request.method == "POST":
		form = BidItemForm(request.POST)
		if form.is_valid():
			bif_form = form.save(commit=False)
			bif_form.save()
			return redirect(reverse('home'))
	else:
		form = BidItemForm()
	return render(request,'make_bid.html', {'form': form})




