from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from rura.models import ICT,InternationalInternetBandwidth,VoiceTraffic
# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"
    def getICTMonthlyReport(self,request):
        ict = ICT.objects.all()
        args ={'ict':ict}
        return render(request,self.template_name,args)

def homePageView(request):
    return HttpResponse("With data")
