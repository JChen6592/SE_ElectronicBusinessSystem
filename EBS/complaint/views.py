from django.shortcuts import render, redirect, HttpResponse
from .forms import ProcessComplaint
from .models import ComplaintForm
from users.models import EntryForm

# Create your views here.
def file_complaint(request):
	if request.method == "POST":
		form = ProcessComplaint(request.POST)
		if form.is_valid():
			fc_form = form.save(commit=False)
			fc_form.witness = request.user
			fc_form.save()
			return redirect('home')
	else:
		form = ProcessComplaint()
	return render(request, 'file_complaint.html', {'form' : form})

def view_complaint(request):
	num_complaints = len(ComplaintForm.objects.filter(culprit_username = request.user.EMPLID))
	user_list = EntryForm.objects.filter(request.user.user_type == 1)
	return render(request,'view_complaints.html', {
		'complaints': ComplaintForm.objects.all(),
		'num_complaints' : num_complaints,
		'user_list' : user_list,
	})

def delete_complaint(request):
	inbox = list(ComplaintForm.objects.filter(culprit_username = request.user.EMPLID))
	if request.method == "POST":
		ComplaintForm.objects.filter(pk = request.POST.get('to-delete')).delete()
		return redirect('delete_complaint')
	return render(request, 'delete_complaints.html', {'inbox' : inbox})

