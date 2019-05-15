from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('sell_post/', views.sell_post, name='sell_post'),
	path('sales/', views.test, name='test'),
	path('s/', views.search, name='search'),
	path('cart/',views.cart, name= 'cart'),
	path('bid_item', views.bid_item, name='bid_item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)