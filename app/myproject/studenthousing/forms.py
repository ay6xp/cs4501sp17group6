from django import forms
from .models import User, Listing


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        exclude = ['joined_date']


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ['post_date']
