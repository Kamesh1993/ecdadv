"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class StateForm(forms.Form):
    states=(['chattisgarh','Chattisgarh'],
             ['mizoram','Mizoram'],
             ['telangana','Telangana'],
             ['madhya pradesh','Madhya Pradesh'],
             ['rajasthan','Rajasthan'])
    dropdown = forms.CharField(label='Please select state', widget=forms.Select(choices=states))

class state_const_form(forms.Form):
    states=(['chattisgarh','Chattisgarh'],
             ['mizoram','Mizoram'],
             ['telangana','Telangana'],
             ['madhya pradesh','Madhya Pradesh'],
             ['rajasthan','Rajasthan'])
    dropdown = forms.CharField(label='Please select state', widget=forms.Select(choices=states))
    dropdown1 = forms.CharField(label='Please select constituency', widget=forms.Select(choices=states))

