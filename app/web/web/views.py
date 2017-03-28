from django.shortcuts import render
import requests
import urllib.request
import urllib.parse
import json
from json import JSONEncoder
from django.template import loader
from django.http import HttpResponseRedirect, JsonResponse
from django.conf import settings
from .forms import RegisterForm
from .forms import LoginForm
from django.core.urlresolvers import reverse


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
        # next = request.GET.get('login') or reverse('index')
        return render(request, 'home/login.html', {'form': login_form, 'auth': auth})
    f = LoginForm(request.POST)
    if not f.is_valid():
        login_form = LoginForm()
        return render(request, 'home/login.html', {'errorMessage': "Please fill out all fields", 'form': login_form})
    username = f.cleaned_data['username']
    password = f.cleaned_data['password']
    response = requests.post(settings.API_DIR + 'login/', data={'username': username, 'password': password}).json()
    if response['ok'] == False:
        # error occurred
        login_form = LoginForm()
        return render(request, 'home/login.html', {'errorMessage': response['resp'], 'form': login_form})
    auth_token = response['resp']
    next = HttpResponseRedirect(reverse('index'))
    next.set_cookie('auth', auth_token)
    return next


def register(request):
    auth = request.COOKIES.get('auth')
    # If we received a GET request instead of a POST request
    if request.method == 'GET':
        # display the login form page
        register_form = RegisterForm()
        return render(request, 'home/register.html', {'form': register_form, 'auth': auth})

    # Creates a new instance of our login_form and gives it our POST data
    f = RegisterForm(request.POST)

    # Check if the form instance is invalid
    if not f.is_valid():
        # Form was bad -- send them back to login page and show them an error
        return render(request, 'home/register.html',
                      {'msg': "Please fill out the registration form again.", 'form': RegisterForm, 'auth': auth})
    else:
        # Sanitize fields
        username = f.cleaned_data['username']
        password = f.cleaned_data['password']
        email = f.cleaned_data['email']
        phone_num = f.cleaned_data['phone_num']

        response = requests.post(settings.API_DIR + 'users/register/', data={'username': username, 'password': password,
                                                                             'email': email,
                                                                             'phone_num': phone_num}).json()

        # Get next page
        next = reverse('login')
        # Check if the experience layer said they gave us incorrect information
        if not response['ok']:
            # Couldn't log them in, send them back to login page with error
            return render(request, 'home/register.html', {'msg': "Invalid signup", 'form': f})
        return HttpResponseRedirect(next)

        """ If we made it here, we can log them in. """
        # Set their login cookie and redirect to back to wherever they came from
        authenticator = resp['resp']['authenticator']

        response = HttpResponseRedirect(next)
        response.set_cookie("auth", authenticator)

        return response
