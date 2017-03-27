from django import forms
from datetime import datetime

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    phone_num = forms.CharField(label='Phone Number', max_length=10, required=True)