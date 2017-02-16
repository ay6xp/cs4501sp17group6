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
			# ...

			new_listing = Listing.objects.create(
				# put data here
			)
			return JsonResponse(model_to_dict(new_listing))

#
#	"read" and "update" functionalities of Listing CRUD
#
@csrf_exempt
def listing_detail(request, id):
	curr_listing = Listing.objects.all().filter(id=id)
	if curr_listing.count() == 1:
		return JsonResponse(list(curr_listing), safe=False)
	else:
		response_data = {}
		response_data['ok'] = 'false'
		response_data['message'] = 'no listing exists with id %s' % id
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
				response_data['message'] = 'user %s successfully created' % id
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
