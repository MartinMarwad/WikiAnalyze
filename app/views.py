from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse
from django.template import Template, Context


def index(request):
    
    return render(request, 'index.html') #, context={'articles': articles},)
