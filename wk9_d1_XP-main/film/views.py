
from .models import *
from .forms import *
from django.views.generic import CreateView, ListView


# Create your views here.

class AddFilmView(CreateView):
    form_class = AddFilmForm
    model = Film
    template_name = 'film/add_film.html'


class AddDirector(CreateView):
    form_class = AddDirector
    model = Director
    template_name = 'film/add_director.html'


class FilmLibrary(ListView):
    model = Film
    template_name = 'film/film_list.html'
    context_object_name = 'film'

    def get_absolute_url(self):
        return reverse('film_list')
