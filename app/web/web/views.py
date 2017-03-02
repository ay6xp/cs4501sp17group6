from django.shortcuts import render
# from .models import Listing
import requests
import urllib.request
import urllib.parse
import json
from json import JSONEncoder
from django.template import loader
from django.http import HttpResponse

def _url(path):
    return 'http://exp-api:8000/api/v1/' + path


def index(request):

    req = requests.get(_url('listings/')).json()
    all_listings = req['info']
    print(req['info'])

    return render(request, 'home/index.html', {'all_listings': all_listings})


def listing_detail(request, id):
    req = requests.get(_url('listings/') + str(id) + '/').json()
    data = req['info']

    return render(request, 'home/listing.html', {'listing': data['fields'], 'pk': data['pk']})
