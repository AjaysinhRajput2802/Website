from django.shortcuts import render,redirect
from .models import participant

# Create your views here.
def participantRg(request):
    if request.method=='POST':
        name = request.POST['eventName']
        number = request.POST['mobile']
        mail = request.POST['email']
        rgT = request.POST['type']
        if rgT=='individual':
            NoPeople=1
        else:
            NoPeople = request.POST['people']
        x=participant.objects.create(name=name,number=number,email=mail,rgType=rgT,NoPeople=NoPeople) 
        x.save()
        return redirect('/')
    return render(request,'participantRg.html')