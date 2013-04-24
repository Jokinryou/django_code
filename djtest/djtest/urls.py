from django.conf.urls import patterns, include, url
from djtest.views import hello, current_datetime, hours_ahead
#from djtest.books import views
from djtest.contact import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djtest.views.home', name='home'),
    # url(r'^djtest/', include('djtest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', hello),
    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    #(r'^search-form/$', views.search),
    #(r'^search/$', views.search),
    (r'^contact/$', views.contact),
    (r'^contact/thanks/$', views.contact_thanks),
)
