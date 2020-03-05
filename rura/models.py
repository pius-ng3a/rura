from django.db import models

# Create your models here.
class ICT(models.Model):
    company_name = models.CharField(max_length=30)
    date_paid = models.DateTimeField(auto_now=False) #necessary to have this cuz recording could be made at a later date than actual payment month
    amount = models.CharField(max_length=20,default=62972)
    postpaid = models.CharField(max_length=30)
    prepaid = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now=True)
    mobile_subscribers = models.CharField(max_length=40)
    fixed_subscribers = models.CharField(max_length=40)
    class Meta:
        ordering = ['created_on']
        def __unicode__(self):
            return self.company_name
class InternationalInternetBandwidth(models.Model):
    company_name = models.CharField(max_length=30)
    up_link = models.CharField(max_length=20)
    down_link = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering =['created_on']
    def __unicode__(self):
        return self.company_name
class VoiceTraffic(models.Model):
    destination = models.CharField(max_length=20)
    company_name = models.CharField(max_length=40)
    call_count = models.CharField(max_length=40)
    out_going = models.BooleanField(default=True)
    average_minute_per_call = models.CharField(max_length=5)
    created_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering =['created_on']
    def __unicode__(self):
        return self.company_name
