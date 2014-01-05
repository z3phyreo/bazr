from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bazr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('market.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^user/', include('registration.backends.default.urls'), name='user'),
    url(r'^foundation/', include('foundation.urls')),
)

urlpatterns +=staticfiles_urlpatterns()
