from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/listings/$', views.get_all_listings, name='get_all_listings'),
    url(r'^api/v1/listings/(?P<id>[0-9]+)/$', views.get_listing, name='get_listing'),
    url(r'^api/v1/users/$', views.get_all_users, name='get_all_users'),
    url(r'^api/v1/users/(?P<id>[0-9]+)/$', views.get_user, name='get_user'),
]
