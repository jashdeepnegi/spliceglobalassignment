from django.urls import path
from accounts.views import *

urlpatterns = [
    path('vendoruserauth/', VendorUserAuth.as_view(), name="VendorUserAuth"),
    path('bidderuserauth/', BidderUserAuth.as_view(), name="BidderUserAuth"),
]