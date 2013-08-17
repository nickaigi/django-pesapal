from django.conf.urls.defaults import patterns, url
from core.views import *


urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^buy/(?P<product_id>\w+)$', buy, name='buy'),
)
