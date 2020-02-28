from django.urls import  path
from . import  views
urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    #path('stats/monthly', name='monthlyStatistics'),
    #path('stats/quarterly',name='quarterlyStatistics')
]
