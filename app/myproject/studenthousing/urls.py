from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# User CRUD
	url(r'^users/$', views.users, name='users'),
	url(r'^users/new/$', views.user_create, name='new_user'),
	url(r'^users/(?P<id>[0-9]+)/$', views.user_detail, name='user_detail'),
	url(r'^users/delete/(?P<id>[0-9]+)/$', views.user_delete, name='delete_user'),
	# Listing CRUD
	url(r'^listings/$', views.listings, name='listings'),
	url(r'^listings/new/$', views.listing_create, name='new_listing'),
	url(r'^listings/(?P<id>[0-9]+)/$', views.listing_detail, name='listing_detail'),
	url(r'^listings/delete/(P<id>[0-9]+)/$', views.listing_delete, name='delete_listing')
]