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
          'pesapal_transaction_tracking_id': '36c1355e-3c5d-4d55-97af-7c6584ef5d65'
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
          'pesapal_merchant_reference': 'KE0C60008',
          'pesapal_transaction_tracking_id': '36c1355e-3c5d-4d55-97af-7c6584ef5d65'
        }

        pesapal_request = client.queryPaymentDetails(params)
        print pesapal_request.to_url()
        pesapal_response_data = requests.get(pesapal_request.to_url())
        print pesapal_response_data.text



if __name__ == '__main__':
    unittest.main()
