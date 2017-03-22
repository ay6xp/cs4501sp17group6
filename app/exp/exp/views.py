import json
import requests
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime, timedelta


def index(request):
	#
	# get all listings & users
	#
	listings_res = requests.get(settings.API_DIR + 'listings/').json()
	users_res = requests.get(settings.API_DIR + 'users/').json()

	#
	# get listings that expire within three days
	#
	exp_soon_list = []

	# check to see if each post's expiration date is within 3 days of now
	for i in range(len(listings_res['info'])):
		# get string representation of post's date
		post_expy_str = listings_res['info'][i]['post_expiration_date']
		# convert into date object
		post_expy_date = datetime.strptime(post_expy_str, '%Y-%m-%d').date()
		
		# check dates
		if post_expy_date <= datetime.now().date() + timedelta(days=3):
			# this is one we should return in this view
			exp_soon_list.append(listings_res['info'][i])
		else:
			# this is not one we should return in this view
			pass

	#
	# get listings posted within the past three days
	#
	l_recent_list = []

	# check to see if each listing was posted within the past three days
	for i in range(len(listings_res['info'])):
		# get string representation of post's date
		posted_str = listings_res['info'][i]['post_date']
		# convert into date object
		posted_date = datetime.strptime(posted_str, '%Y-%m-%d').date()
		
		# check dates
		if posted_date >= datetime.now().date() - timedelta(days=3):
			# this is one we should return in this view
			l_recent_list.append(listings_res['info'][i])
		else:
			# this is not one we should return in this view
			pass

	#
	# get users that joined within the past three days
	#
	u_recent_list = []

	# check to see if each user joined within the past three days
	for i in range(len(users_res['info'])):
		# get string representation of post's date
		joined_str = users_res['info'][i]['joined_date']
		# convert into date object
		joined_date = datetime.strptime(joined_str, '%Y-%m-%d').date()
		
		# check dates
		if joined_date >= datetime.now().date() - timedelta(days=3):
			# this is one we should return in this view
			u_recent_list.append(users_res['info'][i])
		else:
			# this is not one we should return in this view
			pass

	return JsonResponse({'all_listings': listings_res['info'],
						 'all_users': users_res['info'],
						 'exp_soon_listings': exp_soon_list,
						 'recent_listings': l_recent_list,
						 'recent_users': u_recent_list})

#
#	Listings
#
def get_all_listings(request):
	res = requests.get(settings.API_DIR + 'listings/').json()

	if res['ok']:
		return JsonResponse({'info': res['info']})
	else:
		return JsonResponse({'message': res['message']})

def get_listing(request, id):
	res = requests.get(settings.API_DIR + 'listings/' + str(id) + '/').json()

	if res['ok']:
		return JsonResponse({'info': res['info'], 'ok': True})
	else:
		return JsonResponse({'message': res['message'], 'ok': False})

def get_expiring_soon_listings(request):
	res = requests.get(settings.API_DIR + 'listings/').json()

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
	res = requests.get(settings.API_DIR + 'listings/').json()

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
	res = requests.get(settings.API_DIR + 'users/').json()

	if res['ok']:
		return JsonResponse({'info': res['info']})
	else:
		return JsonResponse({'message': res['message']})

def get_user(request, id):
	res = requests.get(settings.API_DIR + 'users/' + str(id) + '/').json()

	if res['ok']:
		return JsonResponse({'info': res['info'], 'ok': True})
	else:
		return JsonResponse({'message': res['message'], 'ok': False})

def get_recently_joined_users(request):
	res = requests.get(settings.API_DIR + 'users/').json()

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