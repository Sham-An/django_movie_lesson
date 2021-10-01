from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("<int:pk>/", views.MovieDetailView.as_view()),
]
