from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.
# admin.site.register(Movie)
# admin.site.register(Person)
@admin.register(Movie) #this is register decorator. admin.site.register(Movie) is not needed when this is used
class MovieAdmin(admin.ModelAdmin):
	"""docstring for MovieAdmin"""
	list_display = ('name','movie_type','studio') # this will cause other fields to get displayed
	ordering = ('-name',) # - is for reverse order. comma at the end very important cuz ordering is a singleton 
	search_fields = ('name','movie_type')
	fieldsets=[
	("Name",{'fields':['name']}),
	("Movie Type",{'fields':['movie_type']}),
	("Studio",{'fields':['studio']}),
	("Manager",{'fields':['manager']}),
	("Icon ",{'fields':['icon']}),
	("Movie",{'fields':['video']}),
	]
class ManagerAdmin(admin.ModelAdmin):
	"""docstring for PersonAdmin"""
	list_display =('manager_name','experience')
	fieldsets=[
	("Manager",{'fields':['manager_name']}),
	("Working Experience",{'fields':['experience']}),
	]
admin.site.register(Manager, ManagerAdmin)
#admin.site.register(Movie,MovieAdmin)
#admin.site.site_header = "Aministration Dashboard" # this changes the default title
