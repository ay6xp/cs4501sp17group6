from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# User CRUD
	url(r'^api/v1/users/$', views.users, name='users'),
	url(r'^api/v1/users/new/$', views.user_create, name='new_user'),
	url(r'^api/v1/users/(?P<id>[0-9]+)/$', views.user_detail, name='user_detail'),
	url(r'^api/v1/users/delete/(?P<id>[0-9]+)/$', views.user_delete, name='delete_user'),
	url(r'^api/v1/users/(?P<username>[\w-]+)/$', views.user_from_name, name='user_from_name'),
	# Listing CRUD
	url(r'^api/v1/listings/$', views.listings, name='listings'),
	url(r'^api/v1/listings/new/$', views.listing_create, name='new_listing'),
	url(r'^api/v1/listings/(?P<id>[0-9]+)/$', views.listing_detail, name='listing_detail'),
	url(r'^api/v1/listings/delete/(?P<id>[0-9]+)/$', views.listing_delete, name='delete_listing'),
	# Authenticator CRUD
	url(r'^api/v1/authenticators/new/$', views.auth_create, name="new_auth"),
	url(r'^api/v1/authenticators/get/(?P<auth_token>[\w.@+-]+)/$', views.get_auth, name="get_auth"),
	url(r'^api/v1/authenticators/get/(?P<auth_token>[\w.@+-]+)/$', views.get_auth_user, name="get_auth_user"),
	url(r'^api/v1/authenticators/delete/$', views.auth_delete, name='delete_auth')
]