from django.urls import path
from . import views

urlpatterns = [
	path('file_complaint/', views.file_complaint, name="file_complaint"),
	path('view_complaint/', views.view_complaint, name="view_complaint"),
	path('delete_complaint/', views.delete_complaint, name="delete_complaint")
]