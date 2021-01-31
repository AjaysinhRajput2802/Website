from django.shortcuts import render

# Create your views here.
def eventDashboard(request):
    return render(request,'eventDashboard.html')