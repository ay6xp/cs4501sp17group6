from django.shortcuts import render
import requests
import urllib.request
import urllib.parse
import json
from json import JSONEncoder
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.conf import settings


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