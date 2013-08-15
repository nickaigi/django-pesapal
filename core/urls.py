from django.conf.urls.defaults import patterns, url
from core.views import *


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    #url(r'paybills/$', 'kussd.views.paybill_numbers', name='paybills'),
)
