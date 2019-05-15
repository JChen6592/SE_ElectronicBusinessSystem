from django.shortcuts import render,redirect
from django.views import generic 
from django.views.generic import ListView
from selling.models import Sell
from ouforms.models import OUForm 
from taboo.models import Taboos
from complaint.models import ComplaintForm

def home(request):
#	authenticated = request.user.is_authenticated 

	to_be_advised = OUForm.objects.filter(status = 1)

	num_advise = len(to_be_advised)

	num_taboo = len(Taboos.objects.all())

	num_complaints = len(ComplaintForm.objects.all())


	context = {
		'sales' : Sell.objects.all().order_by('-date_posted'),
		'num_advise' : num_advise,
		'num_taboo' : num_taboo,
		'num_complaints' : num_complaints,
	}


#	if authenticated:
#		user_type = request.user.user_type
#
#		if (user_type == 0):
#
#			adv_form = OUForm.objects.filter(author = request.user.username)
#			adv_status = 0
#
#			return render(request, 'home.html', {
#				'adv_status': adv_status,
#				})
#		else:
#			to_be_advised = OUForm.objects.filter(status = 1)
#
#			num_advise = len(to_be_advised)
#
#			if request.method == "POST":
#				request.session['selected_id'] = request.POST.get('selected_form')
#
#				return redirect('view_advising_form')
#
#			return render(request, 'home.html', {
#				'num_advise': num_advise
#				})

	return render(request,'home.html', context)

'''
class ProductListView(ListView):
	model = Sell
	template_name = 'home.html'
	context_objects_type = 'sales'
	ordering = ['-date_posted']
'''