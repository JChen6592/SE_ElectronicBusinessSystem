from django.urls import path
from .import views 

urlpatterns = [
	path('add_taboo/', views.add_taboo, name='add_taboo'),
	path('taboo_list/', views.view_taboo, name='view_taboo'),
]