from registration.forms import RegistrationForm
#from django import forms
from django.forms import ModelForm
from myuser.models import MyUser

class MyUserForm(ModelForm):
    """
    Get extra user fields to add to form for django-registation
    """
    class Meta:
        model = MyUser
        fields = ('id_verified',)

RegistrationForm.base_fields.update(MyUserForm.base_fields)
