from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', views.index, name='index'),
    url(r'^home/listing/$', views.listing, name='listing'),
    url(r'^home/user/$', views.user, name='user'),
    url(r'^home/listing/(?P<id>[0-9]+)/$', views.listing_detail, name='listing_detail'),
    url(r'^home/listing/expiring_soon/$', views.listing_exp_soon, name='listing_exp_soon'),
    url(r'^home/listing/recently_posted/$', views.listing_post_recently, name='listing_post_recently'),
    url(r'^home/user/(?P<id>[0-9]+)/$', views.user_detail, name='user_detail'),
    url(r'^home/user/recently_joined/$', views.user_recent, name='user_recent')
    # url(r'^home/error/$', views.call_error, name='error_view')
]
