from django import forms
from .models import User, Listing

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ['username', 'email', 'phone_num', 'password']

class ListingForm(forms.ModelForm):
	class Meta:
		model = Listing
		fields = ['user','title', 'address', 'price', 'description', 'num_of_bedrooms', 
					'num_of_bathrooms', 'sqft', 'lot_size', 'max_occupancy', 
					'availability_start', 'availability_end', 'availability_status',
					'post_expiration_date',
					# tags
					'laundry', 'parking', 'pet_friendly', 'smoking', 'water', 'gas',
					'power', 'wifi', 'wheelchair_access', 'furnished', 'balcony',
					'yard', 'images', 'gym', 'maintenance'
				 ]