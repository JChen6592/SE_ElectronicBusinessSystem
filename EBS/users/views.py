from django.shortcuts import render, redirect
from .forms import EntryForm, ProfileChange
from django.urls import reverse_lazy
from django.views import generic 
from .forms import EntryUserForm

# Create your views here.
class SignUp(generic.CreateView):
	form_class = EntryUserForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'


def view_profile(request):
	return render(request, 'profile.html', {'user': request.user})

def edit_profile(request):
	if request.method == "POST":
		form = ProfileChange(request.POST, instance = request.user)

		if form.is_valid():
			form.save()
			return redirect('view_profile')

	else:
		form = ProfileChange(instance = request.user)
		args = {'form': form}
		return render(request, "edit_profile.html", args)

		
def view_users(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	if q:
		user = EntryForm.objects.filter(username__icontains = q)
		context = {'query':q, 'users': user}
		template = 'searched_user_info.html'   # if the product is found go to detail
	else:
		template =  'home.html'
		context ={}

	return render(request,template, context)

def search_users(request):
	return render(request, 'search_user.html')

def friend_list(request):
    return render(request,'friendlist.html')
