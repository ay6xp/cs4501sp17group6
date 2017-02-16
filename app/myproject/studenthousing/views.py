import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import User, Listing
from .forms import UserForm, ListingForm
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# Create your views here.

def index(request):
	response_data = {}
	response_data['ok'] = 'true'
	response_data['message']  = 'welcome to the studenthousing index'
	return JsonResponse(response_data)

#
#	list all Listings
#
def listings(request):
	# what type of HTTP request was made?
	if request.method == 'GET':
		# GET request

		# are there listings to show?
		listings = Listing.objects.all().values()
		if listings.count() == 0:
			# no, there are no listings
			response_data = {}
			response_data['ok'] = 'true'
			response_data['info'] = 'no listings exist at this time'
			return JsonResponse(response_data)

		else:
			# yes, there are listings
			response_data = {}
			response_data['ok'] = 'true'
			response_data['info'] = list(listings)
			return JsonResponse(response_data)

	else:
		# POST (or other) request
		response_data = {}
		response_data['ok'] = 'false'
		response_data['message'] = 'this action only supports GET requests'
		return JsonResponse(response_data)

#
#	"create" functionality of Listing CRUD
#
@csrf_exempt
def listing_create(request):
	if request.method == 'POST':
		# POST request
		# create a form instance and populate it with data from the request
		form = ListingForm(request.POST)
		if form.is_valid():
			# process data in form.cleaned_data
			user = form.cleaned_data['user']
			title = form.cleaned_data['title']
			address = form.cleaned_data['address']
			price = form.cleaned_data['price']
			description = form.cleaned_data['description']
			num_of_bedrooms = form.cleaned_data['num_of_bedrooms']
			num_of_bathrooms = form.cleaned_data['num_of_bathrooms']
			sqft = form.cleaned_data['sqft']
			lot_size = form.cleaned_data['lot_size']
			max_occupancy = form.cleaned_data['max_occupancy']
			availability_start = form.cleaned_data['availability_start']
			availability_end = form.cleaned_data['availability_end']
			availability_status = form.cleaned_data['availability_status']
			post_expiration_date = form.cleaned_data['post_expiration_date']
			laundry = form.cleaned_data['laundry']
			parking = form.cleaned_data['parking']
			pet_friendly = form.cleaned_data['pet_friendly']
			smoking = form.cleaned_data['smoking']
			water = form.cleaned_data['water']
			gas = form.cleaned_data['gas']
			power = form.cleaned_data['power']
			wifi = form.cleaned_data['wifi']
			wheelchair_access = form.cleaned_data['wheelchair_access']
			furnished = form.cleaned_data['furnished']
			balcony = form.cleaned_data['balcony']
			yard = form.cleaned_data['yard']
			images = form.cleaned_data['images']
			gym = form.cleaned_data['gym']
			maintenance = form.cleaned_data['maintenance']

			post_date = datetime.now()

			new_listing = Listing.objects.create(
				user=user, title=title, address=address, price=price, description=description,
				num_of_bathrooms=num_of_bathrooms, num_of_bedrooms=num_of_bedrooms, sqft=sqft,
				lot_size=lot_size, max_occupancy=max_occupancy, availability_start=availability_start,
				availability_end=availability_end, availability_status=availability_status, 
				post_date=post_date, post_expiration_date=post_expiration_date, laundry=laundry,
				parking=parking, pet_friendly=pet_friendly, smoking=smoking, water=water, gas=gas,
				power=power, wifi=wifi, wheelchair_access=wheelchair_access, furnished=furnished,
				balcony=balcony, yard=yard, images=images, gym=gym, maintenance=maintenance,
				last_edited_date=post_date
			)

			response_data = {}
			response_data['ok'] = 'true'
			response_data['message'] = 'listing %s successfully created' % title
			response_data['info'] = model_to_dict(new_listing)
			return JsonResponse(response_data)

		else:
			# the form isn't valid
			response_data = {}
			response_data['ok'] = 'false'
			response_data['message'] = 'form data was invalid'
			return JsonResponse(response_data)

	else:
		# GET (or other) request
		response_data = {}
		response_data['ok'] = 'false'
		response_data['message'] = 'this action only supports POST requests'
		return JsonResponse(response_data)

#
#	"read" and "update" functionalities of Listing CRUD
#
@csrf_exempt
def listing_detail(request, id):
	# what kind of request was it?
	if request.method == 'POST':
		# POST request
		# create a form instance and populate it with data from the request
		form = ListingForm(request.POST)
		if form.is_valid():
			# process data in form.cleaned_data
			title = form.cleaned_data['title']
			address = form.cleaned_data['address']
			price = form.cleaned_data['price']
			description = form.cleaned_data['description']
			num_of_bedrooms = form.cleaned_data['num_of_bedrooms']
			num_of_bathrooms = form.cleaned_data['num_of_bathrooms']
			sqft = form.cleaned_data['sqft']
			lot_size = form.cleaned_data['lot_size']
			max_occupancy = form.cleaned_data['max_occupancy']
			availability_start = form.cleaned_data['availability_start']
			availability_end = form.cleaned_data['availability_end']
			availability_status = form.cleaned_data['availability_status']
			post_expiration_date = form.cleaned_data['post_expiration_date']
			laundry = form.cleaned_data['laundry']
			parking = form.cleaned_data['parking']
			pet_friendly = form.cleaned_data['pet_friendly']
			smoking = form.cleaned_data['smoking']
			water = form.cleaned_data['water']
			gas = form.cleaned_data['gas']
			power = form.cleaned_data['power']
			wifi = form.cleaned_data['wifi']
			wheelchair_access = form.cleaned_data['wheelchair_access']
			furnished = form.cleaned_data['furnished']
			balcony = form.cleaned_data['balcony']
			yard = form.cleaned_data['yard']
			images = form.cleaned_data['images']
			gym = form.cleaned_data['gym']
			maintenance = form.cleaned_data['maintenance']

			edit_date = datetime.now()

			# does listing already exist??
			if Listing.objects.all().filter(id=id).exists():
				# yes, listing already exists, so update it
				curr_listing = Listing.objects.all().get(id=id)

				curr_listing.title = title
				curr_listing.address = address
				curr_listing.price = price
				curr_listing.description = description
				curr_listing.num_of_bathrooms = num_of_bathrooms
				curr_listing.num_of_bedrooms = num_of_bedrooms
				curr_listing.sqft = sqft
				curr_listing.lot_size = lot_size
				curr_listing.max_occupancy = max_occupancy
				curr_listing.availability_start = availability_start
				curr_listing.availability_end = availability_end
				curr_listing.availability_status = availability_status
				curr_listing.post_expiration_date = post_expiration_date
				curr_listing.last_edited_date = edit_date
				curr_listing.laundry = laundry
				curr_listing.parking = parking
				curr_listing.pet_friendly = pet_friendly
				curr_listing.smoking = smoking
				curr_listing.water = water
				curr_listing.gas = gas
				curr_listing.power = power
				curr_listing.wifi = wifi
				curr_listing.wheelchair_access = wheelchair_access
				curr_listing.furnished = furnished
				curr_listing.balcony = balcony
				curr_listing.yard = yard
				curr_listing.images = images
				curr_listing.gym = gym
				curr_listing.maintenance = maintenance

				curr_listing.save()

				response_data = {}
				response_data['ok'] = 'true'
				response_data['message'] = 'listing %s successfully updated' % id
				response_data['info'] = model_to_dict(curr_listing)
				return JsonResponse(response_data)

			else:
				# no, listing doesn't already exist
				response_data = {}
				response_data['ok'] = 'false'
				response_data['message'] = 'listing %s does not exist' % id
				return JsonResponse(response_data)

		else:
			# the form isn't valid
			response_data = {}
			response_data['ok'] = 'false'
			response_data['message'] = 'form data was invalid'
			return JsonResponse(response_data)

	else:
		# GET (or other) request
		form = ListingForm()
		# does listing exist?
		if Listing.objects.all().filter(id=id).exists():
			# yes, listing already exists, so show listing's data
			curr_listing = Listing.objects.all().get(id=id)
			response_data = {}
			response_data['ok'] = 'true'
			response_data['info'] = model_to_dict(curr_listing)
			return JsonResponse(response_data)

		else:
			# no, listing doesn't exist
			response_data = {}
			response_data['ok'] = 'false'
			response_data['message'] = 'no listing exists with the id %s' % id
			return JsonResponse(response_data)


#
#	"delete" functionality of Listing CRUD
#
@csrf_exempt
def listing_delete(request, id):
	if request.method == 'GET':
		# GET request
		# does this listing exist?
		if Listing.objects.all().filter(id=id).exists():
			# yes, listing exists, so we can delete it
			curr_listing = Listing.objects.all().get(id=id).delete()
			response_data = {}
			response_data['ok'] = 'true'
			response_data['message'] = 'listing %s successfully deleted' % id
			return JsonResponse(response_data)

		else:
			# no, that listing doesn't exist, so we can't delete it
			response_data = {}
			response_data['ok'] = 'false'
			response_data['message'] = 'no listing exists with the id %s' % id
			return JsonResponse(response_data)

	else:
	# POST (or other) request
		response_data = {}
		response_data['ok'] = 'false'
		response_data['message'] = 'this action only supports GET requests'
		return JsonResponse(response_data)


#
#	list all Users
#
def users(request):
	# what type of HTTP request was made?
	if request.method == 'GET':
		# GET request

		# are there users to show?
		users = User.objects.all().values()
		if users.count() == 0:
			# no, there are no users
			response_data = {}
			response_data['ok'] = 'true'
			response_data['info'] = 'no users exist at this time'
			return JsonResponse(response_data)

		else:
			# yes, there are users
			response_data = {}
			response_data['ok'] = 'true'
			response_data['info'] = list(users)
			return JsonResponse(response_data)

	else:
		# POST (or other) request
		response_data = {}
		response_data['ok'] = 'false'
		response_data['message'] = 'this action only supports GET requests'
		return JsonResponse(response_data)


#
#	"create" functionality of User CRUD
#
@csrf_exempt
def user_create(request):
	if request.method == 'POST':
		# POST request
		# create a form instance and populate it with data from the request
		form = UserForm(request.POST)
		if form.is_valid():
			# process data in form.cleaned_data
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			phone_num = form.cleaned_data['phone_num']
			password = form.cleaned_data['password']

			time = datetime.now()

			# let's maintain unique usernames
			if User.objects.all().filter(username=username).count() > 0:
				# some existing user already has this username
				response_data = {}
				response_data['ok'] = 'false'
				response_data['message'] = 'username \'%s\' is already in use' % username
				return JsonResponse(response_data)

			else:
				# no one else already has this username, so we can use it
				new_user = User.objects.create(
					username=username, email=email,
					phone_num=phone_num, password=password,
					joined_date=time
				)

				response_data = {}
				response_data['ok'] = 'true'
				response_data['message'] = 'user %s successfully created' % username
				response_data['info'] = model_to_dict(new_user)
				return JsonResponse(response_data)

		else:
			# the form isn't valid
			response_data = {}
			response_data['ok'] = 'false'
			response_data['message'] = 'form data was invalid'
			return JsonResponse(response_data)

	else:
		# GET (or other) request
		response_data = {}
		response_data['ok'] = 'false'
		response_data['message'] = 'this action only supports POST requests'
		return JsonResponse(response_data)

#
#	"read" and "update" functionalities of User CRUD
#
@csrf_exempt
def user_detail(request, id):
	# what kind of request was it?
	if request.method == 'POST':
		# POST request
		# create a form instance and populate it with data from the request
		form = UserForm(request.POST)
		if form.is_valid():
			# process data in form.cleaned_data
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			phone_num = form.cleaned_data['phone_num']
			password = form.cleaned_data['password']

			# does user already exist??
			if User.objects.all().filter(id=id).exists():
				# yes, user already exists, so update them
				curr_user = User.objects.all().get(id=id)

				# make sure this requested username isn't already in use by someone else
				if User.objects.all().filter(username=username).exists():
					# a user has this name already. we know it's only one because
					# we already checked during user creation.
					# it could be the user who's trying to update things though:
					if User.objects.all().get(username=username) == User.objects.all().get(id=id):
						# it is the same user! they're updating their username to be the 
						# same as it already was. no biggie, we can proceed
						curr_user.username = username
						curr_user.email = email
						curr_user.phone_num = phone_num
						curr_user.password = password
						curr_user.save()

						response_data = {}
						response_data['ok'] = 'true'
						response_data['message'] = 'user %s successfully updated' % id
						response_data['info'] = model_to_dict(curr_user)
						return JsonResponse(response_data)

					else:
						# it's not the same user, which means our user trying to update things
						# would be stealing the name from another user. can't have that
						response_data = {}
						response_data['ok'] = 'false'
						response_data['message'] = 'a user with username \'%s\' already exists' % username
						return JsonResponse(response_data)

			else:
				# no, user doesn't already exist
				response_data = {}
				response_data['ok'] = 'false'
				response_data['message'] = 'user %s does not exist' % id
				return JsonResponse(response_data)

		else:
			# the form isn't valid
			response_data = {}
			response_data['ok'] = 'false'
			response_data['message'] = 'form data was invalid'
			return JsonResponse(response_data)

	else:
		# GET (or other) request
		form = UserForm()
		# does user exist?
		if User.objects.all().filter(id=id).exists():
			# yes, user already exists, so show user's data
			curr_user = User.objects.all().get(id=id)
			response_data = {}
			response_data['ok'] = 'true'
			response_data['info'] = model_to_dict(curr_user)
			return JsonResponse(response_data)

		else:
			# no, user doesn't exist
			response_data = {}
			response_data['ok'] = 'false'
			response_data['message'] = 'no user exists with the id %s' % id
			return JsonResponse(response_data)


#
#	"delete" functionality of User CRUD
#
@csrf_exempt
def user_delete(request, id):
	if request.method == 'GET':
		# GET request
		# does this user exist?
		if User.objects.all().filter(id=id).exists():
			# yes, user exists, so we can delete them
			curr_user = User.objects.all().get(id=id).delete()
			response_data = {}
			response_data['ok'] = 'true'
			response_data['message'] = 'user %s successfully deleted' % id
			return JsonResponse(response_data)

		else:
			# no, that user doesn't exist, so we can't delete them
			response_data = {}
			response_data['ok'] = 'false'
			response_data['message'] = 'no user exists with the id %s' % id
			return JsonResponse(response_data)

	else:
	# POST (or other) request
		response_data = {}
		response_data['ok'] = 'false'
		response_data['message'] = 'this action only supports GET requests'
		return JsonResponse(response_data)
