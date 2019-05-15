from django.urls import path
from . import views

urlpatterns = [
	path('ouform/', views.submit_ouform, name='submit_ouform'),
	path('form_inbox/', views.view_advising_form, name='view_advising_form'),
	path('select_form/', views.select_form, name='select_form'),
	path('confirm_form/', views.confirm_form, name='confirm_form'),
	path('confirm_deny/', views.confirm_deny, name = 'confirm_deny'),
]