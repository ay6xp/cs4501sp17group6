from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', views.index, name='index'),
    url(r'^home/listing/(?P<id>[0-9]+)/$', views.listing_detail, name='listing_detail'),
    # url(r'^home/error/$', views.call_error, name='error_view')
]
