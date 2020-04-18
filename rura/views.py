from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import JsonResponse
from rura.models import ICT,InternationalInternetBandwidth,VoiceTraffic
from datetime import datetime
# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"
    def getICTReport(self,request):
    #def get(self):
        ict = ICT.objects.all()
        vt =VoiceTraffic.objects.all()
        args ={'ict':ict,'vt':vt}
        return render(self.template_name,args)
    
def homePageView(request):
    template_name = "home.html"
    icts = ICT.objects.all()
    vt =VoiceTraffic.objects.all()
    args ={'icts':icts,'vts':vt}

    return render(request, template_name,args)

def getBarChatData(request):
    template_name = "home.html"
    ict = ICT.objects.all()
    vt =VoiceTraffic.objects.all()
    iternationalIB = InternationalInternetBandwidth.objects.all()
    dt = {
        "data":[len(ict),len(vt),len(iternationalIB)],
        "labels":["ICT ","voice Traffic","Intl Bandwidth"]
    }
    return JsonResponse(dt)

def getICT(request):
    icts = ICT.objects.all()
    vals= []
    labs =[]
    for ict in icts: 
        vals.append(ict.prepaid)
        labs.append(datetime.date(ict.date_paid))
       
    dt={
        "data":vals,
        "labels":labs
    }
    return JsonResponse(dt)