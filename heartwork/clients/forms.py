__author__ = 'dimitris'

from django import forms
from .models import Client
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

#http://blackglasses.me/2013/09/17/custom-django-user-model/
class RegistrationForm(forms.ModelForm): #UserCreationForm
    password2 = forms.CharField(max_length=256, label='Repeat Password', help_text='0-10 characters long',
                                widget=forms.PasswordInput({'placeholder': 'Repeat', 'class': 'form-control'}))

    class Meta:
        model = Client
        fields = ['email', 'password', 'password2', 'first_name', 'last_name']
        labels = {
            'email': _('Email'),
            'password': _('Password'),
            'first_name': _('First Name'),
            'last_name': _('Last Name')

        }

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'your_email_address@hostname.com', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'your password', 'type': 'password', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'optional', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'optional', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        the_email=cleaned_data.get('email')
        if 'register' in self.data:
            print("YOU PRESSED IT!!x`")
        print 'DATA --->>>', self.data
        print 'FORM',self.errors
        print 'CONTINUR',self.non_field_errors
        if 'login' in self.data:
            print "I AM LOGING YOU"
        # validate_email(cleaned_data['email'])
        pass1 = cleaned_data.get('password')
        pass2 = cleaned_data.get('password2')
        if pass1 != pass2:
            print 'NOT THE SAME PASSWORDS'
            raise forms.ValidationError(_("NOT THE SAME "))

        return cleaned_data


class LogInForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(LogInForm, self).__init__(request, *args, **kwargs)

    class Meta:
        model = Client
        fields = ['username', 'password']
        widgets = {
            'username': forms.EmailInput(attrs={'placeholder': 'your_email_address@hostname.com'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'your password', 'type': 'password'}),
        }



    def clean(self):
        print("RUnning FORMS clean()")
        cleaned_data = super(AuthenticationForm, self).clean()
        email = cleaned_data.get('username')
        print('-----', cleaned_data, '-----', email)
        client = None
        try:
            client = Client.objects.get(email=email)
        except ObjectDoesNotExist:
            print 'YOU DO NOT EXIST'
            raise forms.ValidationError("YOU CANNOT FIND YOU MAN " + email)
        # return super(LogInForm, self).clean()
        return cleaned_data
