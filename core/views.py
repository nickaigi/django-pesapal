# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from pymongo import MongoClient


def  home(request):
    """
    Home page for django-pesapal example
    """
    jewels = {}
    products = MongoClient()['sasa']['products']
    for product in products.find(limit=3):
        jewel = { 
                    'name': product['name'],
                    'price': product['price'],
                    'thumbnail': product['thumbnail'],
                    'preview': product['preview']
                }
        jewels[product['product_id']] = jewel
    return render_to_response('home.html', {'jewels': jewels}, context_instance=RequestContext(request))


def products_page(request,_id):
    """
    Dispalay product with _id = id
    """
    pass
