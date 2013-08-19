from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pesapal(models.Model):
    """
    Model to hold pesapal callback info
    """
    PESAPAL_STATUS_CHOICES = (
                ('pending', 'Pending'),
                ('completed', 'Completed'),
                ('failed', 'Failed'),
                ('invalid', 'Invalid'),
            )
    tracking_id = models.CharField(max_length=50, verbose_name='Pesapal Transaction Tracking ID')
    product_id = models.CharField(max_length=50, verbose_name='Pesapal Merchant Reference')
    status = models.CharField(max_length=9, choices=PESAPAL_STATUS_CHOICES, default='pending')
    user = models.ForeignKey(User, verbose_name='Paid by')



    class Meta:
        verbose_name = 'Pesapal Payment'
        verbose_name_plural = 'Pesapal Payments'
        
        def __unicode__(self):
            return 'Payment %s for '%(self.status,self.product_id)

