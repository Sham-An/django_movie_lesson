from django.shortcuts import render
from django.views.generic import ListView, DetailView
#from django.views.generic.base import View

from .models import Movie


# Create your views here.

class MoviesView(ListView):

    """список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False) #all()
    #template_name = "movies/movies.html" переименовано в movie_list.html

# (View)
#    def get(self, request):
#        movies = Movie.objects.all()
#        return render(request, "movies/movies.html", {"movie_list": movies})


class MovieDetailView(DetailView):

    """Полное описание фильмов"""
    model = Movie
    slug_field = "url"
#(View)
#    def get(self, request, slug):
#        movie = Movie.objects.get(url=slug)
#        return render(request, "movies/movie_detail.html", {"movie": movie})
