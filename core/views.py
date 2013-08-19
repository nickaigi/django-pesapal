# Create your views here.
import urllib2
from django.shortcuts import render_to_response
from django.template import RequestContext
from pymongo import MongoClient
from bson.objectid import ObjectId
import  pesapal
from django_pesapal.settings import mongo_host, mongo_port
from core.models import Pesapal

products_db = MongoClient(mongo_host, mongo_port)['sasa']['products']
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
    client = pesapal.PesaPal('uvzyNdMvjn6Ir4id+zwcUNT7bKOsp+wY','fXFK6owbt2B00Yq6JscpvKmDm6o=',True)
    request_data = {
            'Amount': str(item['price']),
            'Description': 'Buy %s from shopsoko '%(item['name']),
            'Type': 'MERCHANT',
            'Reference': item['product_id'],
            'Email': 'nickaigi@gmail.com'
            }
    post_params = {
            'oauth_callback': 'http://staging.shopsoko.com/pesapal/process-order'
            }
    pesapal_request = client.postDirectOrder(post_params, request_data)

    return render_to_response('buy.html',
            {
                'product': product,
                'iframe_url': pesapal_request.to_url()
            },
            context_instance=RequestContext(request)
        )

def process_order(request):
    """
    Handle the callback from pesapal
    """
    tracking_id = request.GET.get('pesapal_transaction_tracking_id', '')
    product_id = request.GET.get('pesapal_merchant_reference', '')
    #save this data to a model
    errors = ''
    if tracking_id and product_id:
        params = {
                    'pesapal_merchant_reference': product_id,
                    'pesapal_transaction_tracking_id': tracking_id
                 }
        client = pesapal.PesaPal('uvzyNdMvjn6Ir4id+zwcUNT7bKOsp+wY','fXFK6owbt2B00Yq6JscpvKmDm6o=',True)
        request = client.queryPaymentStatus(params)
        url = request.to_url()
        print url
        response = urllib2.urlopen(url)
        print response.read()
        #p_ref = Pesapal(tracking_id=tracking_id, product_id=product_id, status='', user='1')
        #p_ref.save()
    else:
        errors ='You broke our servers :-('
    return render_to_response('process-order.html', {'errors': errors}, context_instance=RequestContext(request))

    

