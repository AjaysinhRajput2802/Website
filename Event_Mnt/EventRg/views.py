from django.shortcuts import render,redirect
from .models import event

# Create your views here.
def eventRegistration(request):
    if request.method=='POST':
        name = request.POST['eventName']
        dcr = request.POST['description']
        lc = request.POST['location']
        start = request.POST['start']
        end = request.POST['end']
        dl = request.POST['deadline']
        ml = request.POST['mail']
        pwd = request.POST['password']
        x=event.objects.create(name=name,description=dcr,location=lc,fromDt=start,toDt=end,deadline=dl,mail=ml,pwd=pwd) 
        x.save()
        return redirect('/')
    return render(request,'eventRegistration.html')