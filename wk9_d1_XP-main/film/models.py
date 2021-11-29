from django.db import models
from django.urls import reverse

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Director(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"

    def get_absolute_url(self):
        return reverse('add_director')


class Film(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField(auto_now_add=True)
    created_in_country = models.ForeignKey(Country, on_delete= models.CASCADE, related_name= 'films_made_in')
    available_in_countries = models.ManyToManyField(Country)
    categories = models.ManyToManyField(Category)
    directors = models.ManyToManyField(Director)

    def get_absolute_url(self):
        return reverse('film_lib')

    def __str__(self):
        return f"{self.title} {self.directors} {self. categories} {self.release_date}"
