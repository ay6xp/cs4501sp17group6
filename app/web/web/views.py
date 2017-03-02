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

    req = requests.get('http://exp-api:8000/api/v1/listings/').json()
    all_listings = req['info']
    print(req['info'])

    return render(request, 'home/index.html', {'all_listings': all_listings})

    # req = urllib.request.Request(_url('listings/'))
    # resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    # all_listings = json.loads(resp_json)

    # template = loader.get_template('home/index.html')
    # context = {'all_listings': all_listings}
    # return HttpResponse(template.render(context, request))


def listing_detail(request, id):
    req = requests.get(_url('listings/') + str(id) + '/').json()
    new_req = json.dumps(req)
    listing = req['info']
    # print(type(req)) # type is dict
    # print(type(req['info'])) # type is str
    # print(type(data)) # type is list
    data = json.loads(req['info'])
    print(type(data[0])) # type is dict!!!!!
    print(data[0]['fields'])

    return render(request, 'home/listing.html', {'listing': data[0]['fields']})
