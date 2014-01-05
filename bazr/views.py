from registration.backends.default.views import RegistrationView
from registration import signals
from registration.models import RegistrationProfile
from django.contrib.sites.models import Site
from django.contrib.sites.models import RequestSite

class CustomRegistrationView(RegistrationView):
    """
    Needed override this django-registration feature to have it create
    a profile with extra field
    """
    def register(self, request, **cleaned_data):
        username, email, password, addr_street= cleaned_data['username'], cleaned_data['email'], cleaned_data['password1'], cleaned_data['addr_street']
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        new_user = RegistrationProfile.objects.create_inactive_user(
            username, email, password, addr_street, site)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user
