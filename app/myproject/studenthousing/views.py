from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
	return HttpResponse("Welcome to the studenthousing index.")

def listings(request):
	return HttpResponse("Here are all of the listings.")

def listing_detail(request, listing_id):
	return HttpResponse("This is the listing with id %s." % listing_id)

def user_list(request):
	return HttpResponse("Here are all of the users.")
