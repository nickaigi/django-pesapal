from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from core.models import Pesapal

class PesapalAdmin(admin.ModelAdmin):
    list_display = ('user','product_id', 'status',)
    search_fields = ('product_id', 'user',)
    list_filter = ('status', )

admin.site.register(Pesapal, PesapalAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)
