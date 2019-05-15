from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from .forms import OUEntryForm
from .models import OUForm
from users.models import EntryForm

def submit_ouform(request):
	if request.method == "POST":
		form = OUEntryForm(request.POST)
		if form.is_valid():
			a_form = form.save(commit=False)
			a_form.author = request.user.username
			a_form.status = 1
			a_form.date_submitted = timezone.now()
			request.user.was_denied = False 
			request.user.save()
			a_form.save()
			return redirect('home')
	else:
		form = OUEntryForm()
	return render(request, 'submit_ouform.html', {'form':form})

def select_form(request):
	to_be_advised = OUForm.objects.filter(status=1)
	if request.method == "POST":
		request.session['selected_id'] = request.POST.get('selected_form')

		return redirect('view_advising_form')
	return render(request,'select_form.html', {'to_be_advised': to_be_advised})

def view_advising_form(request):
	a_form = OUForm.objects.get(pk = request.session['selected_id'])
	f_name = EntryForm.objects.get(username = a_form.author).first_name
	l_name = EntryForm.objects.get(username = a_form.author).last_name

	return render(request, 'view_advising_form.html', {
		'subject': a_form.subject,
		'username': a_form.author,
		'f_name': f_name,
		'l_name': l_name,
		'email': a_form.email,
		'address': a_form.address, 
		})

def confirm_form(request):
	a_form = OUForm.objects.get(pk = request.session['selected_id'])
	u_name = EntryForm.objects.get(username = a_form.author) 
	if (request.user.user_type == 2):
		if request.method == "POST":
			a_form.status = 2
			u_name.user_type = 1
			u_name.save()
			a_form.save() 
			request.session['selected_id'] = ''
			return redirect('home')
	return render(request, 'confirm_form.html', {'a_form': a_form})

def confirm_deny(request):
	a_form = OUForm.objects.get(pk = request.session['selected_id'])
	GU = EntryForm.objects.get(username = a_form.author)
	if request.method == "POST":
		GU.was_denied = True
		GU.save()
		a_form.delete()
		request.session['selected_id'] = ''
		return redirect('home')
	return render(request, 'confirm_deny.html', { 
		'a_form' : a_form 
	})







