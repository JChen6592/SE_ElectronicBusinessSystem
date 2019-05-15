from django.urls import path 
from . import views

urlpatterns = [
	path('signup/',views.SignUp.as_view(), name='signup'),
	path('profile/', views.view_profile, name='view_profile'),
	path('edit_profile/',views.edit_profile, name='edit_profile'),
	path ('search_user/',views.search_users , name = 'search_user' ),
	path ('searcheduserinfo/', views.view_users, name = 'searcheduserinfo'),
	path ('friendlist/', views.friend_list, name = 'friendlist')
]
