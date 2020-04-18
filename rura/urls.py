from django.urls import  path
from . import  views
from rura.views import getBarChatData,getICT
#from django.contrib.auth.views import login
#from rura.views import home, contact

urlpatterns = [
    #path('',views.HomePageView.as_view(),name='home'),
    path('',views.homePageView,name="home"),
    path('get/patient/bar/data',getBarChatData,name="chart_data"),
    path('get/prepaid/ict/data',getICT,name="ict_prepaid")
    #path('stats/monthly', name='monthlyStatistics'),
    #path('stats/quarterly',name='quarterlyStatistics')
]
