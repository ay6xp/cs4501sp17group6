import json
import urllib.request
import urllib.parse
from django.http import JsonResponse

#
#	helper function for url construction
#
def _url(path):
	return 'http://models-api:8000/studenthousing/api/v1/' + path

#
#	Listings
#
def get_all_listings(request):
	req = urllib.request.Request(_url('listings/'))
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	res = json.loads(resp_json)

	if res['ok']:
		return JsonResponse({'info': res['info']})
	else:
		return JsonResponse({'message': res['message']})

def get_listing(request, id):
	req = urllib.request.Request(_url('listings/') + str(id) + '/')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	res = json.loads(resp_json)

	if res['ok']:
		return JsonResponse({'info': res['info']})
	else:
		return JsonResponse({'message': res['message']})

def get_expiring_soon_listings(request):
	req = urllib.request.Request(_url('listings/expiring_soon/'))
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	res = json.loads(resp_json)
	pass


#
#	Users
#
def get_all_users(request):
	req = urllib.request.Request(_url('users/'))
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	res = json.loads(resp_json)

	if res['ok']:
		return JsonResponse({'info': res['info']})
	else:
		return JsonResponse({'message': res['message']})

def get_user(request, id):
	req = urllib.request.Request(_url('users/') + str(id) + '/')
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	res = json.loads(resp_json)

	if res['ok']:
		return JsonResponse({'info': res['info']})
	else:
		return JsonResponse({'message': res['message']})

def create_user(request):
	pass

def get_active_users(request):
	pass

def get_recently_joined_users(request):
	pass