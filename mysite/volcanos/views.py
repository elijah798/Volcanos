from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'volcanos/Japan3.html')

# Create your views here.
