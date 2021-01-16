from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html')

def event_registration(request):
    return render(request,'event_registration.html')

def participant_rg(request):
    return render(request,'participant_rg.html')

def event_dashboard(request):
    return render(request,'event_dashboard.html')
