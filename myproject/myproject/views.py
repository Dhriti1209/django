from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    #return HttpResponse("Hello this is our homepage")
    return render(request,'website/index.html')
def about(Request):
    return HttpResponse("Hello this is our aboutpage")
def contact(Request):
    return HttpResponse("Hello this is our contactpage")