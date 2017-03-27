import json

from django.http import JsonResponse
from .models import User, Listing
from .forms import UserForm, ListingForm
from django.core import serializers
from django.forms.models import model_to_dict
from datetime import datetime
import os
import hmac
from django.conf import settings

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
			response_data['ok'] = True
			response_data['message'] = 'no listings exist at this time'
			return JsonResponse(response_data)

		else:
			# yes, there are listings
			response_data = {}
			response_data['ok'] = True
			response_data['info'] = list(listings)
			return JsonResponse(response_data)

	else:
		# POST (or other) request
		response_data = {}
		response_data['ok'] = False
		response_data['message'] = 'this action only supports GET requests'
		return JsonResponse(response_data)

#
#	"create" functionality of Listing CRUD
#
def listing_create(request):
	if request.method == 'POST':
		# POST request
		# create a form instance and populate it with data from the request
		form = ListingForm(request.POST)
		if form.is_valid():

			new_listing = form.save()
			data = serializers.serialize('json', [new_listing])
			data_as_list = json.loads(data)

			response_data = {}
			response_data['ok'] = True
			response_data['message'] = 'listing %s successfully created' % id
			response_data['info'] = data_as_list[0]
			return JsonResponse(response_data)

		else:
			# the form isn't valid
			response_data = {}
			response_data['ok'] = False
			response_data['message'] = 'form data was invalid: %s' % form.errors
			return JsonResponse(response_data)

	else:
		# GET (or other) request
		response_data = {}
		response_data['ok'] = False
		response_data['message'] = 'this action only supports POST requests'
		return JsonResponse(response_data)

#
#	"read" and "update" functionalities of Listing CRUD
#
def listing_detail(request, id):
	# what kind of request was it?
	if request.method == 'POST':
		# POST request
		# create a form instance and populate it with data from the request
		form = ListingForm(request.POST)
		if form.is_valid():

			# does listing already exist??
			if Listing.objects.all().filter(id=id).exists():
				# yes, listing already exists, so update it
				l = Listing.objects.all().get(id=id)
				data = serializers.serialize('json', [l])
				data_as_list = json.loads(data)

				f = ListingForm(request.POST, instance=l)
				f.save()

				response_data = {}
				response_data['ok'] = True
				response_data['message'] = 'listing %s successfully updated' % id
				response_data['info'] = data_as_list[0]
				return JsonResponse(response_data)

			else:
				# no, listing doesn't already exist
				response_data = {}
				response_data['ok'] = False
				response_data['message'] = 'listing %s does not exist' % id
				return JsonResponse(response_data)

		else:
			# the form isn't valid
			response_data = {}
			response_data['ok'] = False
			response_data['message'] = form.errors
			return JsonResponse(response_data)

	else:
		# GET (or other) request
		form = ListingForm()
		# does listing exist?
		if Listing.objects.all().filter(id=id).exists():
			# yes, listing already exists, so show listing's data
			l = Listing.objects.all().get(id=id)
			data = serializers.serialize('json', [l])
			data_as_list = json.loads(data)
			response_data = {}
			response_data['ok'] = True
			response_data['info'] = data_as_list[0]
			return JsonResponse(response_data)

		else:
			# no, listing doesn't exist
			response_data = {}
			response_data['ok'] = False
			response_data['message'] = 'no listing exists with the id %s' % id
			return JsonResponse(response_data)


#
#	"delete" functionality of Listing CRUD
#
def listing_delete(request, id):
	if request.method == 'GET':
		# GET request
		# does this listing exist?
		if Listing.objects.all().filter(id=id).exists():
			# yes, listing exists, so we can delete it
			curr_listing = Listing.objects.all().get(id=id).delete()
			response_data = {}
			response_data['ok'] = True
			response_data['message'] = 'listing %s successfully deleted' % id
			return JsonResponse(response_data)

		else:
			# no, that listing doesn't exist, so we can't delete it
			response_data = {}
			response_data['ok'] = False
			response_data['message'] = 'no listing exists with the id %s' % id
			return JsonResponse(response_data)

	else:
	# POST (or other) request
		response_data = {}
		response_data['ok'] = False
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
			response_data['ok'] = True
			response_data['message'] = 'no users exist at this time'
			return JsonResponse(response_data)

		else:
			# yes, there are users
			response_data = {}
			response_data['ok'] = True
			response_data['info'] = list(users)
			return JsonResponse(response_data)

	else:
		# POST (or other) request
		response_data = {}
		response_data['ok'] = False
		response_data['message'] = 'this action only supports GET requests'
		return JsonResponse(response_data)


#
#	"create" functionality of User CRUD
#
def user_create(request):
	if request.method == 'POST':
		# POST request
		# create a form instance and populate it with data from the request
		form = UserForm(request.POST)
		if form.is_valid():
			# get username for ease of use
			username = form.cleaned_data['username']

			# let's maintain unique usernames
			if User.objects.all().filter(username=username).count() > 0:
				# some existing user already has this username
				response_data = {}
				response_data['ok'] = False
				response_data['message'] = 'username \'%s\' is already in use' % username
				return JsonResponse(response_data)

			else:
				# no one else already has this username, so we can use it
				new_user = form.save()

				response_data = {}
				response_data['ok'] = True
				response_data['message'] = 'user %s successfully created' % username
				response_data['info'] = model_to_dict(new_user)
				return JsonResponse(response_data)

		else:
			# the form isn't valid
			response_data = {}
			response_data['ok'] = False
			response_data['message'] = 'form data was invalid'
			return JsonResponse(response_data)

	else:
		# GET (or other) request
		response_data = {}
		response_data['ok'] = False
		response_data['message'] = 'this action only supports POST requests'
		return JsonResponse(response_data)

#
#	"read" and "update" functionalities of User CRUD
#
def user_detail(request, id):
	# what kind of request was it?
	if request.method == 'POST':
		# POST request
		# create a form instance and populate it with data from the request
		form = UserForm(request.POST)
		if form.is_valid():
			# get username for ease of use
			username = form.cleaned_data['username']

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
						f = UserForm(request.POST, instance=curr_user)
						f.save()

						response_data = {}
						response_data['ok'] = True
						response_data['message'] = 'user %s successfully updated' % id
						response_data['info'] = model_to_dict(curr_user)
						return JsonResponse(response_data)

					else:
						# it's not the same user, which means our user trying to update things
						# would be stealing the name from another user. can't have that
						response_data = {}
						response_data['ok'] = False
						response_data['message'] = 'a user with username \'%s\' already exists' % username
						return JsonResponse(response_data)

			else:
				# no, user doesn't already exist
				response_data = {}
				response_data['ok'] = False
				response_data['message'] = 'user %s does not exist' % id
				return JsonResponse(response_data)

		else:
			# the form isn't valid
			response_data = {}
			response_data['ok'] = False
			response_data['message'] = 'form data was invalid'
			return JsonResponse(response_data)

	else:
		# GET (or other) request
		form = UserForm()
		# does user exist?
		if User.objects.all().filter(id=id).exists():
			# yes, user already exists, so show user's data
			u = User.objects.all().get(id=id)
			data = serializers.serialize('json', [u])
			data_as_list = json.loads(data)
			response_data = {}
			response_data['ok'] = True
			response_data['info'] = data_as_list[0]
			return JsonResponse(response_data)

		else:
			# no, user doesn't exist
			response_data = {}
			response_data['ok'] = False
			response_data['message'] = 'no user exists with the id %s' % id
			return JsonResponse(response_data)


#
#	"delete" functionality of User CRUD
#
def user_delete(request, id):
	if request.method == 'GET':
		# GET request
		# does this user exist?
		if User.objects.all().filter(id=id).exists():
			# yes, user exists, so we can delete them
			curr_user = User.objects.all().get(id=id).delete()
			response_data = {}
			response_data['ok'] = True
			response_data['message'] = 'user %s successfully deleted' % id
			return JsonResponse(response_data)

		else:
			# no, that user doesn't exist, so we can't delete them
			response_data = {}
			response_data['ok'] = False
			response_data['message'] = 'no user exists with the id %s' % id
			return JsonResponse(response_data)

	else:
	# POST (or other) request
		response_data = {}
		response_data['ok'] = False
		response_data['message'] = 'this action only supports GET requests'
		return JsonResponse(response_data)

#
#	"create" functionality of Authenticator CRUD
#
def auth_create(request):
	if request.method == 'POST':
		# POST request
		# create a form instance and populate it with data from the request
		form = UserForm(request.POST)
		if 'user_id' in request.POST:
			# get user id for ease of use
			u_id = request.POST['user_id']

			# does authenticator exist for this user?
			auth_obj = Authenticator.objects.filter(user_id=u_id)

			if auth_obj.exists():
				# yep it exists! woohoo
				response_data = {}
				response_data['ok'] = True
				response_data['info'] = auth_obj[0].authenticator
				return JsonResponse(response_data)

			else:
				# one doesn't exist, so we need to make it
				auth_token = hmac.new(
					key = settings.SECRET_KEY.encode('utf-8'),
					msg = os.urandom(32),
					digestmod = 'sha256',
				).hexdigest()

				preexisting = False
				# by some probabilistic miracle, did this token already exist?
				if Authenticator.objects.filter(authenticator=auth_token).exists():
					# yes indeedy
					preexisting = True

				# keep remaking it until there's no hash collision
				while preexisting:
					auth_token = hmac.new(
						key = settings.SECRET_KEY.encode('utf-8'),
						msg = os.urandom(32),
						digestmod = 'sha256',
					).hexdigest()

					if Authenticator.objects.filter(authenticator=auth_token).exists():
						preexisting = True
					else:
						preexisting = False

				# we have a unique token now
				new_auth_obj = Authenticator.objects.create(
					authenticator = auth_token,
					user_id = u_id
				)

				response_data = {}
				response_data['ok'] = True
				response_data['message'] = 'authenticator for user %s successfully created' % u_id
				response_data['info'] = auth_token
				return JsonResponse(response_data)

		else:
			# the form isn't valid
			response_data = {}
			response_data['ok'] = False
			response_data['message'] = 'no user id included'
			return JsonResponse(response_data)

	else:
		# GET (or other) request
		response_data = {}
		response_data['ok'] = False
		response_data['message'] = 'this action only supports POST requests'
		return JsonResponse(response_data)

#
#	"read" functionality of Authenticator CRUD
#
def get_auth(request, auth_token):
	# what type of HTTP request was made?
	if request.method == 'GET':
		# GET request

		# does the authenticator exist?
		if Authenticator.objects.filter(authenticator=auth_token).exists():
			response_data = {}
			response_data['ok'] = True
			response_data['message'] = 'this authenticator exists'
			return JsonResponse(response_data)
		else:
			response_data = {}
			response_data['ok'] = False
			response_data['message'] = 'this authenticator does not exist'
			return JsonResponse(response_data)

	else:
		# POST (or other) request
		response_data = {}
		response_data['ok'] = False
		response_data['message'] = 'this action only supports GET requests'
		return JsonResponse(response_data)

def get_auth_user(request, auth_token):
	# what type of HTTP request was made?
	if request.method == 'GET':
		# GET request

		# does the authenticator exist?
		if Authenticator.objects.filter(authenticator=auth_token).exists():
			response_data = {}
			response_data['ok'] = True
			response_data['message'] = 'this authenticator exists'
			response_data['info'] = Authenticator.objects.filter(authenticator=auth_token)[0].user_id
			return JsonResponse(response_data)
		else:
			response_data = {}
			response_data['ok'] = False
			response_data['message'] = 'this authenticator does not exist'
			return JsonResponse(response_data)

	else:
		# POST (or other) request
		response_data = {}
		response_data['ok'] = False
		response_data['message'] = 'this action only supports GET requests'
		return JsonResponse(response_data)

#
#	"delete" functionality of Authenticator CRUD
#
def auth_delete(request):
	if request.method == 'POST':
		# POST request

		if 'auth_token' in request.POST:
			# it exists, so delete it
			try:
				Authenticator.objects.filter(authenticator=request.POST['auth_token']).delete()
			except:
				response_data = {}
				response_data['ok'] = False
				response_data['message'] = 'authenticator deletion failed'
				return JsonResponse(response_data)

			response_data = {}
			response_data['ok'] = True
			response_data['message'] = 'authenticator successfully deleted'

		else:
			# invalid POST request
			response_data = {}
			response_data['ok'] = False
			response_data['message'] = 'no authenticator was specified'
			return JsonResponse(response_data)

	else:
		# GET (or other) request
		response_data = {}
		response_data['ok'] = False
		response_data['message'] = 'this action only supports POST requests'
		return JsonResponse(response_data)