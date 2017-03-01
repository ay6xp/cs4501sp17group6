from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # listings
    url(r'^api/v1/listings/$', views.get_all_listings, name='get_all_listings'),
    url(r'^api/v1/listings/(?P<id>[0-9]+)/$', views.get_listing, name='get_listing'),
    url(r'^api/v1/listings/expiring_soon/$', views.get_expiring_soon_listings, name='get_expiring_soon_listings'),
    url(r'^api/v1/listings/recently_posted/$', views.get_recently_posted_listings, name='get_recently_posted_listings'), 

    # users
    url(r'^api/v1/users/$', views.get_all_users, name='get_all_users'),
    url(r'^api/v1/users/(?P<id>[0-9]+)/$', views.get_user, name='get_user'),
    url(r'^api/v1/users/recently_joined/$', views.get_recently_joined_users, name='get_recently_joined_users'),
]
