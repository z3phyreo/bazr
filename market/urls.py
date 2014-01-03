from django.conf.urls import patterns, url, include
import market.views

urlpatterns = patterns('',
        url(r'^listings$', market.views.ListingList.as_view(), name='listings',),
        url(r'^new$', market.views.ListingNew.as_view(), name='listing-new'),
)
