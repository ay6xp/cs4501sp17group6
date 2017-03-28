import json
import requests
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime, timedelta
from django.contrib.auth import hashers


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

    #
    # use this opportunity to delete expired authenticators
    # since the home page will get frequent traffic
    #
    auths_res = requests.get(settings.API_DIR + 'authenticators/').json()

    # check to see if each post's expiration date is within 3 days of now
    for i in range(len(auths_res['info'])):
        # get string representation of auth's date
        created_str_dt = auths_res['info'][i]['date_created']
        created_str_d = created_str_dt[:-14]
        # convert into date object
        created_date = datetime.strptime(created_str_d, '%Y-%m-%d').date()

        # check dates
        if created_date <= datetime.now().date() - timedelta(days=2):
            # this is one we should delete
            requests.post(settings.API_DIR + 'authenticators/delete/',
                          data={'auth_token': auths_res['info'][i]['authenticator']})
        else:
            # this is not one we should delete
            pass

    return JsonResponse(
        {'all_listings': listings_res['info'], 'all_users': users_res['info'], 'exp_soon_listings': exp_soon_list,
         'recent_listings': l_recent_list, 'recent_users': u_recent_list})


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


def new_listing(request):
    title = request.POST.get('title', 'default')
    address = request.POST.get('address', 'default')
    residence_type = request.POST.get('residence_type', 'default')
    num_of_bedrooms = request.POST.get('num_of_bedrooms', 'default')
    num_of_bathrooms = request.POST.get('num_of_bathrooms', 'default')
    price = request.POST.get('price', 'default')
    sqft = request.POST.get('sqft', 'default')
    lot_size = request.POST.get('lot_size', 'default')
    max_occupancy = request.POST.get('max_occupancy', 'default')
    availability_start = request.POST.get('availability_start', 'default')
    availability_end = request.POST.get('availability_end', 'default')
    availability_status = request.POST.get('availability_status', 'default')
    description = request.POST.get('description', 'default')
    post_expiration_date = request.POST.get('post_expiration_date', 'default')
    laundry = request.POST.get('laundry', 'default')
    parking = request.POST.get('parking', 'default')
    pet_friendly = request.POST.get('pet_friendly', 'default')
    smoking = request.POST.get('smoking', 'default')
    water = request.POST.get('water', 'default')
    gas = request.POST.get('gas', 'default')
    power = request.POST.get('power', 'default')
    wifi = request.POST.get('wifi', 'default')
    wheelchair_access = request.POST.get('wheelchair_access', 'default')
    furnished = request.POST.get('furnished', 'default')
    balcony = request.POST.get('balcony', 'default')
    yard = request.POST.get('yard', 'default')
    images = request.POST.get('images', 'default')
    gym = request.POST.get('gym', 'default')
    maintenance = request.POST.get('maintenance', 'default')
    try:
        auth = request.POST.get('auth')
    except:
        response_data = {}
        response_data['ok'] = False
        response_data['message'] = 'unauthenticated user'
        return JsonResponse(response_data)

    # get authenticated user's id
    response = requests.get(settings.API_DIR + 'authenticators/get_auth_user/' + auth + '/').json()
    if not response['ok']:
        return JsonResponse(response)
    else:
        user = response['info']
        resp = requests.post(settings.API_DIR + 'listings/new/', data={
            'title': title,
            'address': address,
            'residence_type': residence_type,
            'num_of_bedrooms': num_of_bedrooms,
            'num_of_bathrooms': num_of_bathrooms,
            'price': price,
            'sqft': sqft,
            'lot_size': lot_size,
            'max_occupancy': max_occupancy,
            'availability_start': availability_start,
            'availability_end': availability_end,
            'availability_status': availability_status,
            'description': description,
            'post_expiration_date': post_expiration_date,
            'laundry': laundry,
            'parking': parking,
            'pet_friendly': pet_friendly,
            'smoking': smoking,
            'water': water,
            'gas': gas,
            'power': power,
            'wifi': wifi,
            'wheelchair_access': wheelchair_access,
            'furnished': furnished,
            'balcony': balcony,
            'yard': yard,
            'images': images,
            'gym': gym,
            'maintenance': maintenance,
            'user': user}).json()
    return JsonResponse(resp)


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
    return JsonResponse({'message': res['message']})


def logout(request):
    auth = request.POST.get('auth', 'default')
    response = requests.post(settings.API_DIR + 'authenticators/delete/', data={'auth': auth}).json()
    return JsonResponse(response)


def register(request):
    username = request.POST.get('username', 'none')
    password = request.POST.get('password', 'none')
    email = request.POST.get('email', 'none')
    phone_num = request.POST.get('phone_num', 'none')
    user = requests.post(settings.API_DIR + 'users/new/',
                         data={'username': username, 'password': password, 'email': email,
                               'phone_num': phone_num}).json()
    return JsonResponse(user, safe=False)


def login(request):
    username = request.POST.get('username', 'none')
    pass_attempt = request.POST.get('password', 'none')

    resp = requests.get(settings.API_DIR + 'users/' + username + '/').json()

    if resp['ok']:
        curr_user = resp['info']
        curr_pass = curr_user['password']

        if hashers.check_password(pass_attempt, curr_pass):
            # passwords match! create an authenticator
            auth_response = requests.post(settings.API_DIR + 'authenticators/new/',
                                          data={"user_id": curr_user['pk']}).json()
            return JsonResponse(auth_response)
        else:
            response_data = {}
            response_data['ok'] = False
            response_data['message'] = 'invalid password'
            return JsonResponse(response_data)
    return JsonResponse(resp)
