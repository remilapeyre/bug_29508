from django import forms
from django.contrib.admin import forms as admin_forms
from django.contrib.auth.forms import UsernameField
from django.utils.translation import gettext_lazy as _


class AdminAuthenticationForm(admin_forms.AdminAuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'class': 'form-control',
        'placeholder': _('Username')
    }))
