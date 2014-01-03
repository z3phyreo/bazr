#from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView

#from django.views.decorators.cache import cache_page
#from django.http import HttpResponse, HttpResponseRedirect, Http404
from market.models import Listing

# Create your views here.

#@cache_page (60 * 5)
class ListingList(ListView):

    model = Listing
    template_name = 'listings.html'

class ListingNew(CreateView):

    model = Listing

    fields = ['title','listing_type','description']

    template_name = 'listing_new.html'

    def get_success_url(self):
        return reverse('listings')

