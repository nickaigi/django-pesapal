# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from pymongo import MongoClient
from bson.objectid import ObjectId


products_db = MongoClient()['sasa']['products']
def home(request):
    """
    Home page for django-pesapal example
    """
    products = []
    for item in products_db.find(limit=3):
       product = {
                   'name': item['name'],
                   'price': item['price'],
                   'thumbnail': item['thumbnail'],
                   'preview': item['preview'],
                   'product_id': item['_id']
               }
       products.append(product)
    return render_to_response('home.html', {'products': products}, context_instance=RequestContext(request))


def buy(request,product_id):
    """
    Buy product with _id = product_id
    """
    item = products_db.find_one({'_id': ObjectId(product_id)})
    product = {
                'name': item['name'],
                'price': item['price'],
                'thumbnail': item['thumbnail'],
                'preview': item['preview'],
                'product_id': item['_id']
            }
    return render_to_response('buy.html', {'product': product}, context_instance=RequestContext(request))

