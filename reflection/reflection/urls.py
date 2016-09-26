from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views
import core.views

# Examples:
# url(r'^$', 'scrs.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
url(r'^$', hello.views.IndexView.as_view(), name='index'),
    url(r'hello/', include('hello.urls')),
    url(r'core/', include('core.urls')),
    url(r'mfp/', include('mfp.urls')),
    url(r'eula/', include('eulag.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
