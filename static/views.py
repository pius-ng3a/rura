from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Movie,Manager,MovieForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .forms import AddMovieForm
class MovieView(TemplateView):
	"""docstring for MovieView"""
	template_name="movie.html"
	def get_context_data(self, *args, **kwargs):
		context = super(MovieView, self).get_context_data(**kwargs)
		movies = Movie.objects.all()
		persons = Manager.objects.all()
		context['movies'] = movies
		context['persons']=persons
		return context
	
class PlayMovie(TemplateView):
	"""docstring for PlayMovie"""
	template_name="play.html"

def movie_play(request,movieid):
	movie =Movie.objects.get(pk = movieid)
	manager = Manager.objects.get(pk = movie.manager_id)
	return render(request, 'play.html',{"movie":movie,'manager':manager})
		
def save_created_movie(request):
	if request.method == "POST":
		form = MovieForm(request.POST,request.FILES)
		if form.is_valid(): #check that the form has all fields specified as needed
			form.save()
			return redirect('movie/')
		else:
			form = MovieForm()
			return render(request,'edit_movie.html',{'form':form})
def create_new_movie(request):
	form = MovieForm(request.POST,request.FILES)
	return render(request,'addmovie.html',{'form':form})

class MovieFormView(CreateView):
	form_class = AddMovieForm
	template_name = 'addmovie.html'
	#success_url =''
def delete(request,movieid):
	Movie.objects.get(pk=movieid).delete()
	return redirect('movie')
def edit_movie(request,movieid):
	
	instance = Movie.objects.get(pk=movieid)
	if request.method == "POST":
		form =MovieForm(request.POST,request.FILES, instance=instance)
		if form.is_valid():
			form.save()
			return redirect("movie")
	else:
		form = MovieForm(instance=instance)
		return render(request,'edit_movie.html',{'form':form})