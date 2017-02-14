from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# User CRU(D)
	url(r'^users/$', views.users, name='users'),
	url(r'^users/(?P<username>\w+)/$', views.user_detail, name='user_detail'),
	# Listing CRU(D)
	url(r'^listings/$', views.listings, name='listings'),
	url(r'^listings/(?P<listing_id>[0-9]+)/$', views.listing_detail, name='listing_detail'),
]