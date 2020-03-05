from time import time

from django import forms
from .models import Movie,Manager
from django.shortcuts import redirect
def get_upload_file_name(instance,filename): #function to rename files and give a unique name
    return "uploaded_files/%s_%s"%(str(time()).replace('.','_'),filename)

class DateInput(forms.DateInput):
    """docstring for DateInput"""
    input_type = 'date'
class AddMovieForm(forms.ModelForm):
    manager = forms.CharField(max_length= 25)
    class Meta:
        model = Movie
        fields = ['name','movie_type','studio','manager','icon','video']
        # widgets ={
        #     'created_at':DateInput(attrs={'type':'date'}),
        #     'updated_at':DateInput(attrs={'type':'date'}),
        # }
    def clean(self):
        cleaned_data = super(AddMovieForm, self).clean()
        name = cleaned_data.get('name')
        movie_type = cleaned_data.get('movie_type')
        studio = cleaned_data.get('studio')
        #created_at = cleaned_data.get('created_at')
        icon = cleaned_data.get('icon')
        video = cleaned_data.get('video')
        #updated_at = cleaned_data.get('updated_at')
        manager = cleaned_data.get('manager')
        if not name and not movie_type and not manager and not video and not icon and not studio:
            raise forms.ValidationError('You have to write something!')
        manager = self.cleaned_data.pop("manager")
        new_manager,created = Manager.objects.get_or_create(manager_name=manager,defaults={'experience':1})
        self.cleaned_data.update({'manager':new_manager})
    def save(self, commit=True):
        # try:
        #     self.cleaned_data['manager'] = Manager.objects.get(manager_name=manager) 

        # except DoesNotExists:   
        #     new_namager = Manager.objects.create(manager_name =manager,experience=1)
        #     new_namager.save()
        #     self.cleaned_data['manager']=new_namager
        #     print(new_namager.manager_name, " NEW MANAGER")
        # else:
        #     print("Failed to create new manager object")
        # finally:
        #     pass
        # manager_fetched, created = Manager.objects.get_or_create(
        #     manager_name=self.cleaned_data['manager'],
        #     defaults={'experience': 1}
        # )
        # if created:
        #     manager_fetched.save()
        # self.cleaned_data['manager'] = manager_fetched.id
        return super(AddMovieForm, self).save(commit)
