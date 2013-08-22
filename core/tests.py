#!/usr/bin/env python
import unittest
import pesapal
import requests

KEY = 'uvzyNdMvjn6Ir4id+zwcUNT7bKOsp+wY'
SECRET = 'fXFK6owbt2B00Yq6JscpvKmDm6o='

class TestPesapal(unittest.TestCase):

    def setUp(self):
        self.client = pesapal.PesaPal(KEY, SECRET, True)

    def test_query_payment_status(self):
        """
        determine the payment status
        """

        client = self.client

        params = {
          'pesapal_merchant_reference': 'KE0C60008',
          'pesapal_transaction_tracking_id': '8712e0bd-bbf1-4c50-a0a9-56b3019e7cc6'
        }

        pesapal_request = client.queryPaymentStatus(params)
        print pesapal_request.to_url()
        pesapal_response_data = requests.get(pesapal_request.to_url())
        print pesapal_response_data.text

    def test_query_payment_status_by_merchant_ref(self):

        client = self.client

        params = {
          'pesapal_merchant_reference': 'KE0C60008'
        }

        pesapal_request = client.queryPaymentStatusByMerchantRef(params)
        print pesapal_request.to_url()
        pesapal_response_data = requests.get(pesapal_request.to_url())
        print pesapal_response_data.text


    def test_query_payment_details(self):

        client = self.client

        params = {
          'pesapal_merchant_reference': '000',
          'pesapal_transaction_tracking_id': '000'
        }

        pesapal_request = client.queryPaymentDetails(params)
        print pesapal_request.to_url()
        pesapal_response_data = requests.get(pesapal_request.to_url())
        print pesapal_response_data.text



if __name__ == '__main__':
    unittest.main()
