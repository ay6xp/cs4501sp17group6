import json
import urllib.request
import urllib.parse
from django.http import JsonResponse
from datetime import datetime, timedelta

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
	req = urllib.request.Request(_url('listings/'))
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	res = json.loads(resp_json)

	if res['ok']:

		exp_soon_list = []

		# check to see if each post's expiration date is within 3 days of now
		for i in range(len(res['info'])):
			# get string representation of post's date
			post_expy_str = res['info'][i]['post_expiration_date']
			# convert into date object
			post_expy_date = datetime.strptime(post_expy_str, '%Y-%m-%d').date()
			
			# check dates
			if post_expy_date <= datetime.now().date() + timedelta(days=3):
				# this is one we should return in this view
				exp_soon_list.append(res['info'][i])
			else:
				# this is not one we should return in this view
				pass

		# is list empty?
		if len(exp_soon_list) == 0:
			return JsonResponse({'message': 'no listings expire within 3 days'})

		return JsonResponse({'info': exp_soon_list})

	else:
		return JsonResponse({'message': res['message']})

def get_recently_posted_listings(request):
	req = urllib.request.Request(_url('listings/'))
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	res = json.loads(resp_json)

	if res['ok']:

		recent_list = []

		# check to see if each listing was posted within the past three days
		for i in range(len(res['info'])):
			# get string representation of post's date
			posted_str = res['info'][i]['post_date']
			# convert into date object
			posted_date = datetime.strptime(posted_str, '%Y-%m-%d').date()
			
			# check dates
			if posted_date >= datetime.now().date() - timedelta(days=3):
				# this is one we should return in this view
				recent_list.append(res['info'][i])
			else:
				# this is not one we should return in this view
				pass

		# is list empty?
		if len(recent_list) == 0:
			return JsonResponse({'message': 'no new listings were posted in the last 3 days'})

		return JsonResponse({'info': recent_list})

	else:
		return JsonResponse({'message': res['message']})


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
	req = urllib.request.Request(_url('users/'))
	resp_json = urllib.request.urlopen(req).read().decode('utf-8')
	res = json.loads(resp_json)

	if res['ok']:

		recent_list = []

		# check to see if each user joined within the past three days
		for i in range(len(res['info'])):
			# get string representation of post's date
			joined_str = res['info'][i]['joined_date']
			# convert into date object
			joined_date = datetime.strptime(joined_str, '%Y-%m-%d').date()
			
			# check dates
			if joined_date >= datetime.now().date() - timedelta(days=3):
				# this is one we should return in this view
				recent_list.append(res['info'][i])
			else:
				# this is not one we should return in this view
				pass

		# is list empty?
		if len(recent_list) == 0:
			return JsonResponse({'message': 'no new users have joined in the last 3 days'})

		return JsonResponse({'info': recent_list})

	else:
		return JsonResponse({'message': res['message']})