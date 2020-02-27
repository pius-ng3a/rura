from django.urls import  path
from . import  views
urlpatterns = [
    path('',views.homePageView,name='home'),
    #path('stats/monthly', name='monthlyStatistics'),
    #path('stats/quarterly',name='quarterlyStatistics')
]
