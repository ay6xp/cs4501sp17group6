from django import forms
from .models import User, Listing

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User

class ListingForm(forms.ModelForm):
	class Meta:
		model = Listing