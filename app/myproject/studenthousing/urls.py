from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# User CRUD
	url(r'^users/$', views.user_list, name='user_list'),
	# Listing CRUD
	url(r'^listings/$', views.listings, name='listings'),
	url(r'^listings/(?P<listing_id>[0-9]+)/$', views.listing_detail, name='listing_detail'),
]