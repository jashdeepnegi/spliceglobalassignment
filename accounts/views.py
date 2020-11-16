from django.shortcuts import render

# Create your views here.

from appspliceglobal.models import Vendor, Bidder
from accounts.serializers import VendorSerializers, BidderSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class VendorUserAuth(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        vendorUsers = Vendor.objects.all()
        serializer = VendorSerializers(vendorUsers, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            first_name = request.POST.get("first_name")
            print(first_name)
            company_name = request.POST.get("company_name")
            print(company_name)
        serializer = VendorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BidderUserAuth(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, *args, **kwargs):
        bidderUsers = Bidder.objects.all()
        serializer = BidderSerializers(bidderUsers, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = BidderSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)