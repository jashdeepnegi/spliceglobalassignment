from django.shortcuts import render
from django.http import HttpResponse
from .choice import *
# Create your views here.
def index(request):
    return render(request, 'appspliceglobal/index.html', {'country_name': COUNTRY})

