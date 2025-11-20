from django.shortcuts import render

def all_newapp(request):
    return render(request,'newapp/all_newapp.html')
