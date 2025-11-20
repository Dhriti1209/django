from django.http import HttpResponse
from django.shortcuts import render
def home(Request):
    return HttpResponse("Hello this is our homepage")
def about(Request):
    return HttpResponse("Hello this is our aboutpage")
def contact(Request):
    return HttpResponse("Hello this is our contactpage")