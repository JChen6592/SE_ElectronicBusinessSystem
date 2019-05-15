from django.shortcuts import render, redirect, HttpResponse
from .forms import TabooWordEntry
from .models import Taboos

# Create your views here.
def add_taboo(request):
	if request.method == "POST":
		form = TabooWordEntry(request.POST)
		if form.is_valid():
			t_form = form.save(commit=False)
			t_form.save()
			return redirect('home')
	else:
		form = TabooWordEntry()
	return render(request, 'add_taboo_word.html', {'form': form})

def view_taboo(request):
	num_taboo = len(Taboos.objects.all())
	return render(request, 'view_taboo_list.html', {
		'taboowords' : Taboos.objects.all(),
		'num_taboo' : num_taboo,
	})

def delete_taboo(request):
	inbox = list(Taboos.objects.all())
	if request.method == "POST":
		Taboos.object.filter(pk = request.POST.get('to-delete')).delete()
		return redirect('delete_taboo')
	return render(request, 'delete_taboo.html', {'inbox': inbox})
