import json
import requests
from django.http import JsonResponse

#
#	helper function for url construction
#
def _url(path):
	return 'http://models-api:8000/api/v1/' + path

#
#	Listings
#
def get_all_listings(request):
	# step one: make get request
	# step two: get JSON object from response
	r = requests.get(_url('listings/')).json()
	# if no errors, return the data
	if r['ok']:
		return JsonResponse({'info': r['info']})
	# if errors, return the error message
	else:
		return JsonResponse({'message': r['message']})

def get_listing(request, listing_id):
	r = requests.get(_url('listings/') + str(listing_id) + '/').json()
	if r['ok']:
		return JsonResponse({'info': r['info']})
	else:
		return JsonResponse({'message': r['message']})


#
#	Users
#
def get_all_users(request):
	r = requests.get(_url('users/')).json()
	if r['ok']:
		return JsonResponse({'info': r['info']})
	else:
		return JsonResponse({'message': r['message']})

def get_user(request, user_id):
	r = requests.get(_url('users/') + str(user_id) + '/').json()
	if r['ok']:
		return JsonResponse({'info': r['info']})
	else:
		return JsonResponse({'message': r['message']})