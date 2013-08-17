from django.db import models

# Create your models here.
class PesaPalRef(models.Model):
    """
    Model to hold pesapal callback info
    """
    tracking_id = models.CharField(max_length=50, verbose_name='Pesapal Transaction Tracking ID')
    product_id = models.CharField(max_length=50, verbose_name='Pesapal Merchant Reference')

    class Meta:
        verbose_name_plural = 'PesaPal Refs'
        def __unicode__(self):
            return self.product_id

