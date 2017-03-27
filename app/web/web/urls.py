from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', views.index, name='index'),
    url(r'^home/listings/$', views.listing, name='listing'),
    url(r'^home/listings/(?P<id>[0-9]+)/$', views.listing_detail, name='listing_detail'),
    url(r'^home/listings/expiring_soon/$', views.listing_exp_soon, name='exp_soon_listings'),
    url(r'^home/listings/recently_posted/$', views.listing_post_recently, name='recent_listings'),
    url(r'^home/users/$', views.user, name='user'),
    url(r'^home/users/(?P<id>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^home/users/recently_joined/$', views.user_recent, name='users_recent'),
    url(r'^register/$', views.register, name='register'),
]
