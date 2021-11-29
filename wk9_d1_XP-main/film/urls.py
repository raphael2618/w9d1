
from django.urls import path
from . import views

urlpatterns = [

    path('add_film/', views.AddFilmView.as_view(), name='add_film'),
    path('add_director/', views.AddDirector.as_view(), name='add_director'),
    path('films/', views.FilmLibrary.as_view(), name='film_lib')

]
