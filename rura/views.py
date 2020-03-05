from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from rura.models import ICT,InternationalInternetBandwidth,VoiceTraffic
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
