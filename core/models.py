from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pesapal(models.Model):
    """
    Model to hold pesapal callback info
    """
    #<PENDING|COMPLETED|FAILED|INVALID>
    PESAPAL_STATUS_CHOICES = (
                ('PENDING', 'Pending'),
                ('COMPLETED', 'Completed'),
                ('FAILED', 'Failed'),
                ('INVALID', 'Invalid'),
            )
    tracking_id = models.CharField(max_length=50, verbose_name='Pesapal Transaction Tracking ID')
    reference = models.CharField(max_length=50, verbose_name='Pesapal Merchant Reference')
    status = models.CharField(max_length=9, choices=PESAPAL_STATUS_CHOICES, default='PENDING')

    class Meta:
        verbose_name = 'Pesapal Payment'
        verbose_name_plural = 'Pesapal Payments'
        
        def __unicode__(self):
            return 'Payment %s for '%(self.status,self.reference)

