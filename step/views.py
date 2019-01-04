from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import template

# Create your views here.
def index(request):
 return render(request,"step/index.html") 