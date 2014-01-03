from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from myuser.models import MyUser
from django import forms

# Register your models here.

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = MyUser

#our custom user creation form does not have all the fields, more work is needed is adding user from the admin panel is neede. 

class MyUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            MyUser.objects.get(username=username)
        except MyUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreateForm
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ['id_verified']}),)
            #,'addr_street','addr_state','addr_zip','addr_country','time_zone','phone','joined']})    

admin.site.register(MyUser, MyUserAdmin)
