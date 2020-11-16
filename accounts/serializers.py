from rest_framework import serializers

from appspliceglobal.models import Vendor, Bidder

class VendorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class BidderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bidder
        fields = '__all__'