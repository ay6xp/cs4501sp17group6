from django.shortcuts import render
import requests
import urllib.request
import urllib.parse
import json
from json import JSONEncoder
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .forms import RegisterForm, LoginForm, ListingForm


def index(request):
    req = requests.get(settings.API_DIR + 'index/').json()
    return render(request, 'home/index.html', req)

def listing(request):
    req = requests.get(settings.API_DIR + 'listings/').json()
    all_listings = req['info']
    return render(request, 'home/listing.html', {'all_listings': all_listings})

def listing_exp_soon(request):
    req = requests.get(settings.API_DIR + 'listings/expiring_soon/').json()
    print(req)
    return JsonResponse(req)

def listing_post_recently(request):
    req = requests.get(settings.API_DIR + 'listings/recently_posted/').json()
    print(req)
    return JsonResponse(req)

def listing_detail(request, id):
    req = requests.get(settings.API_DIR + 'listings/' + str(id) + '/').json()
    if req['ok']:
        data = req['info']

        return render(request, 'home/listing_detail.html', {'listing': data['fields'], 'pk': data['pk']})
    else:
        return render(request, 'home/error.html', {'msg': 'Listing with ID %s does not exist.' % id})


def user(request):
    req = requests.get(settings.API_DIR + 'users/').json()
    all_users = req['info']
    return render(request, 'home/user.html', {'all_users': all_users})

def user_recent(request):
    req = requests.get(settings.API_DIR + 'users/recently_joined/').json()
    print(req)
    return JsonResponse(req)

def user_detail(request, id):
    req = requests.get(settings.API_DIR + 'users/' + str(id) + '/').json()
    if req['ok']:
        data = req['info']

        return render(request, 'home/user_detail.html', {'user': data['fields'], 'pk': data['pk']})
    else:
        return render(request, 'home/error.html', {'msg': 'User with ID %s does not exist.' % id})

def login(request):
    auth = request.COOKIES.get('auth')
    if auth:
        return render(request, 'home/index.html', auth)
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'home/login.html', {'form':login_form, 'auth':auth})
    f = LoginForm(request.POST)
    if not f.is_valid():
        login_form = LoginForm()
        return render(request, 'home/login.html', {'errorMessage': "Please fill out all fields",'form': login_form})
    username = f.cleaned_data['username']
    password = f.cleaned_data['password']
    response = requests.post('http://exp-api:8000/api/v1/login/', data={'username':username, 'password':password}).json()
    if  response['ok'] == False:
        #error occurred
        login_form = LoginForm()
        return render(request, 'home/login.html', {'errorMessage': response['resp'],'form': login_form})
    auth_token = response['resp']
    next = HttpResponseRedirect(reverse('index'))
    next.set_cookie('auth',auth_token)
    return next

def register(request):
    auth = request.COOKIES.get('auth')
    # If we received a GET request instead of a POST request
    if request.method =='GET':
        # display the login form page
        register_form = RegisterForm()
        return render(request, 'home/register.html', {'form': register_form, 'auth':auth})

    # Creates a new instance of our registration form and gives it our POST data
    f = RegisterForm(request.POST)

    # Check if the form instance is invalid
    if not f.is_valid():
        # Form was bad -- send them back to registration page and show them an error
        return render(request, 'home/register.html', {'msg': 'Please fill out all required fields.', 'form': RegisterForm, 'auth':auth})
    else:
        # # Sanitize fields
        # username = f.cleaned_data['username']
        # password = f.cleaned_data['password']
        # email = f.cleaned_data['email']
        # phone_num = f.cleaned_data['phone_num']
        # joined_date = f.cleaned_data['joined_date']

        # response = requests.post(settings.API_DIR + 'users/register/', data={'username': username, 'password': password, 'email': email, 'phone_num': phone_num, 'joined_date':joined_date}).json()
        # print(response)

        # # Get next page
        # next = reverse('login')
        # # Check if the experience layer said they gave us incorrect information
        # if not response['ok']:
        #     # Couldn't log them in, send them back to login page with error
        #     return render(request, 'home/register.html', {'msg': "Invalid signup", 'form': f})
        # return HttpResponseRedirect(next)

        # """ If we made it here, we can log them in. """
        # # Set their login cookie and redirect to back to wherever they came from
        # authenticator = resp['resp']['authenticator']

        # response = HttpResponseRedirect(next)
        # response.set_cookie("auth", authenticator)

        # return response
        # pass
        return render(request, 'home/index.html')

def listing_new(request):
    auth = request.COOKIES.get('auth')

    if not auth:
        return HttpResponseRedirect(reverse('login') + "?next=" + reverse("new_listing"))

    # what kind of request?
    if request.method == 'GET':
        form = ListingForm()
        return render(request, 'home/new_listing.html', {'form': form, 'auth': auth})

    else:
        form = ListingForm(request.POST)
        if not form.is_valid():
            form = ListingForm()
            return render(request, 'home/new_listing.html', {'form': form, 'auth': auth, 'msg': 'Invalid information provided.'})
        else:
            title = form.cleaned_data['title']
            address = form.cleaned_data['address']
            residence_type = form.cleaned_data['residence_type']
            num_of_bedrooms = form.cleaned_data['num_of_bedrooms']
            num_of_bathrooms = form.cleaned_data['num_of_bathrooms']
            price = form.cleaned_data['price']
            sqft = form.cleaned_data['sqft']
            lot_size = form.cleaned_data['lot_size']
            max_occupancy = form.cleaned_data['max_occupancy']
            availability_start = form.cleaned_data['availability_start']
            availability_end = form.cleaned_data['availability_end']
            availability_status = form.cleaned_data['availability_status']
            description = form.cleaned_data['description']
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

            response = requests.post(settings.API_DIR + 'listings/new/', data={
                'title':title,
                'address':address,
                'residence_type':residence_type,
                'num_of_bedrooms':num_of_bedrooms,
                'num_of_bathrooms':num_of_bathrooms,
                'price':price,
                'sqft':sqft,
                'lot_size':lot_size,
                'max_occupancy':max_occupancy,
                'availability_start':availability_start,
                'availability_end':availability_end,
                'availability_status':availability_status,
                'description':description,
                'post_expiration_date':post_expiration_date,
                'laundry':laundry,
                'parking':parking,
                'pet_friendly':pet_friendly,
                'smoking':smoking,
                'water':water,
                'gas':gas,
                'power':power,
                'wifi':wifi,
                'wheelchair_access':wheelchair_access,
                'furnished':furnished,
                'balcony':balcony,
                'yard':yard,
                'images':images,
                'gym':gym,
                'maintenance':maintenance
            }).json()

            if not response['ok']:
                return render(request, 'home/new_listing.html', {'msg': response['message'], 'form':form, 'auth':auth})
            response = HttpResponseRedirect('/')
            return response
