
from django.conf.urls import patterns, include, url

from api.views import *

urlpatterns = patterns('api.views',
    url(r'^$', ApiRoot.as_view(), name='api-root'),
)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^helloworld/', HelloWorld.as_view(), name='helloworld'),
)

