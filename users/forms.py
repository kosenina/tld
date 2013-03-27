__author__ = 'Luka'

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from users.models import Users

class RegistrationForm(ModelForm):
    username = forms.CharField(label=(u'User Name'))
    email = forms.EmailField(label=(u'Email Address'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = Users
        exclude = ('user',)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("That username is already taken, please select another.")

    def clean(self):
        tmp = self.cleaned_data.get('password')
        tmp1 = self.cleaned_data.get('password1')

        if not tmp or not tmp1:
            raise forms.ValidationError("The password filed cannot be blank.")

        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError("The passwords did not match.  Please try again.")
        return self.cleaned_data

