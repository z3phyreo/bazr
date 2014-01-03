from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from market.models import Listing, Bid

# Register your models here.

admin.site.register(Listing)
admin.site.register(Bid)


