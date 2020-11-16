from django.contrib import admin
from appspliceglobal.models import Vendor, Bidder

# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email1', 'email2', 'password1', 'password2', 'company_name', 'mobile_number',
    'telephone_number', 'address1', 'address2', 'city', 'postal_zip', 'country', 'state')


class BidderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email1', 'email2', 'password1', 'password2')

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Bidder, BidderAdmin)