from django.contrib import admin
from core.models import Pesapal

class PesapalAdmin(admin.ModelAdmin):
    list_display = ('product_id',)
    search_fields = ('product_id', )

admin.site.register(Pesapal, PesapalAdmin)


