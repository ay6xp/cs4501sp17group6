from django import forms
from datetime import datetime

class RegisterForm(forms.Form):

    class Meta:
        username = forms.CharField(label='Username: ', max_length=50, required=True)
        password = forms.CharField(label='Password: ', max_length=50, required=True)
        email = forms.EmailField(label='Email:', max_length=50, required=True)
        phone_num = forms.CharField(label='Phone Number: ', max_length=10, required=True)
        joined_date = forms.DateTimeField(initial=datetime.now(), required=True)