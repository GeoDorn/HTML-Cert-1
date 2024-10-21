from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home_page(request):
    survey = loader.get_template('base.html')
    return HttpResponse(survey.render())