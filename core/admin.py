from django.contrib import admin
from core.models import Pesapal

class PesapalAdmin(admin.ModelAdmin):
    list_display = ('user','product_id', 'status',)
    search_fields = ('product_id', 'user',)
    list_filter = ('status', )

admin.site.register(Pesapal, PesapalAdmin)


