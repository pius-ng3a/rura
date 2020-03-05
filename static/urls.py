from . import views
from django.urls import path

urlpatterns =[
	path('',views.MovieView.as_view(),name='movie'),
	path('<int:movieid>/play',views.movie_play,name='play'),
	path("add",views.MovieFormView.as_view(),name="create_movie"),
	path('<int:movieid>/delete',views.delete,name='delete_movie'),
	path('<int:movieid>/edit',views.edit_movie,name="edit_movie")
]