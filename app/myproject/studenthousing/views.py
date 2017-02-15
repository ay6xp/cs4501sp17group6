import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from .models import User, Listing

# Create your views here.

def index(request):
	return HttpResponse("Welcome to the studenthousing index.")

def listings(request):
	listings = Listing.objects.all().values()
	if listings.count() == 0:
		response_data = {}
		response_data['result'] = 'error'
		response_data['message'] = 'No listings exist at this time.'
		return JsonResponse(response_data)
	return JsonResponse(list(listings), safe=False)

def listing_detail(request, listing_id):
	curr_listing = Listing.objects.all().filter(id=listing_id)
	if curr_listing.count() == 1:
		return JsonResponse(list(curr_listing), safe=False)
	else:
		response_data = {}
		response_data['result'] = 'error'
		response_data['message'] = 'No listing exists with id %s.' % listing_id
		return JsonResponse(response_data)

def users(request):
	users = User.objects.all().values('username', 'email')
	if users.count() == 0:
		response_data = {}
		response_data['result'] = 'error'
		response_data['message'] = 'No users exist at this time.'
		return JsonResponse(response_data)
	else:
		return JsonResponse(list(users), safe=False)

def user_detail(request, username):
	curr_user = User.objects.all().filter(username=username)
	if curr_user.count() == 1:
		return JsonResponse(list(curr_user), safe=False)
	else:
		response_data = {}
		response_data['result'] = 'error'
		response_data['message'] = 'No user exists with username %s.' % username
		return JsonResponse(response_data)