from django import forms
from datetime import datetime

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput())
    email = forms.EmailField(max_length=50, required=True)
    phone_num = forms.IntegerField(label='Phone Number', required=True)
    joined_date = forms.DateField()

class LoginForm(forms.Form):
	username = forms.CharField(max_length=50, required=True)
	password = forms.CharField(widget=forms.PasswordInput(), required=True)

class ListingForm(forms.Form):
	title = forms.CharField(max_length=200)
	address = forms.CharField(max_length=200)
	TYPE_CHOICES = (
        ("A", "Apartment"),
        ("H", "House"),
        ("R", "Room"),
        ("S", "Studio"),
        ("T", "Townhouse"),
        ("O", "Other")
    )
	residence_type = forms.ChoiceField(choices=TYPE_CHOICES)
	num_of_bedrooms = forms.IntegerField()
	num_of_bathrooms = forms.IntegerField()
	price = forms.IntegerField()
	sqft = forms.IntegerField()
	LOT_CHOICES = (
		("S", "Small"),
		("M", "Medium"),
		("L", "Large")
	)
	lot_size = forms.ChoiceField(choices=LOT_CHOICES)
	max_occupancy = forms.IntegerField()
	availability_start = forms.DateField()
	availability_end = forms.DateField()
	AVAILABILITY_CHOICES = (
		("AVAIL", "Available"),
		("SOLD", "Sold")
	)
	availability_status = forms.ChoiceField(choices=AVAILABILITY_CHOICES)
	description = forms.CharField(widget=forms.Textarea())
	post_expiration_date = forms.DateField()

	laundry = forms.BooleanField()
	parking = forms.BooleanField()
	pet_friendly = forms.BooleanField()
	smoking = forms.BooleanField()
	water = forms.BooleanField()
	gas = forms.BooleanField()
	power = forms.BooleanField()
	wifi = forms.BooleanField()
	wheelchair_access = forms.BooleanField()
	furnished = forms.BooleanField()
	balcony = forms.BooleanField()
	yard = forms.BooleanField()
	images = forms.BooleanField()
	gym = forms.BooleanField()
	maintenance = forms.BooleanField()