# Create your views here.
import requests
import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
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
    

    return render_to_response('buy.html',
            {
                'product': product,
            },
            context_instance=RequestContext(request)
        )


def checkout(request):
    """
    """
    delivery_fee = 0 
    if request.method == 'POST':
        product_id = request.POST.get('product_id', '')
        cost = int(request.POST.get('cost', ''))
        delivery_option = request.POST.get('delivery','')
        if delivery_option == 'd':
            delivery_fee = 300
            total_cost = cost + delivery_fee 
        else:
            total_cost = cost

        client = pesapal.PesaPal('uvzyNdMvjn6Ir4id+zwcUNT7bKOsp+wY','fXFK6owbt2B00Yq6JscpvKmDm6o=',True)
        request_data = {
            'Amount': str(total_cost),
            'Description': 'Purchase of jewelry from shopsoko.com',
            'Type': 'MERCHANT',
            'Reference': str(datetime.datetime.now()),
            'Email': 'info@shopsoko.com'
            }
        post_params = {
            'oauth_callback': 'http://staging.shopsoko.com/pesapal/process-order'
            }
        pesapal_request = client.postDirectOrder(post_params, request_data)
        return render_to_response('checkout.html', {
                'total_cost': total_cost,
                'cost': cost,
                'delivery_fee': delivery_fee,
                'iframe_url': pesapal_request.to_url()
                }, context_instance=RequestContext(request))


def process_order(request):
    """
    Handle the callback from pesapal
    """
    tracking_id = request.GET.get('pesapal_transaction_tracking_id', '')
    reference = request.GET.get('pesapal_merchant_reference', '')
    #save this data to a model
    errors = ''
    msg = ''
    if tracking_id and product_id:
        params = {
                    'pesapal_merchant_reference': product_id,
                    'pesapal_transaction_tracking_id': tracking_id
                 }
        client = pesapal.PesaPal('uvzyNdMvjn6Ir4id+zwcUNT7bKOsp+wY','fXFK6owbt2B00Yq6JscpvKmDm6o=',True)
        pesapal_request = client.queryPaymentStatus(params)
        url = pesapal_request.to_url()
        print url
        pesapal_response = requests.get(url)
        pesapal_response_data = pesapal_response.text
        print pesapal_response_data
        pesapal_status = pesapal_response_data.split('=')[1]
        if pesapal_status == 'COMPLETED':
            msg = 'Transaction was successful'
        else:
            msg = 'Transaction status is %s'%(pesapal_status)
        p_ref = Pesapal(tracking_id=tracking_id, reference=reference, status=pesapal_status)
        p_ref.save()
    else:
        errors ='You broke our servers :-('
    return render_to_response('process-order.html', {'errors': errors, 'msg': msg}, context_instance=RequestContext(request))

