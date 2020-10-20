from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length= 30)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length= 30)
    def __str__(self):
        return self.name

class Director(models.Model):
    first_name= models.CharField(max_length= 30)
    last_name= models.CharField(max_length= 30)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Film(models.Model):
    title= models.CharField(max_length= 30, unique= True)
    release_date= models.DateField(auto_now_add= True)
    created_in_country= models.ForeignKey(Country, on_delete=models.CASCADE, related_name= 'created_films')
    available_in_countries= models.ManyToManyField(Country, related_name='available_films')
    category= models.ManyToManyField(Category)
    director= models.ManyToManyField(Director)
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = 
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

# f= Film()
# f.available_in_countries.all()
# c= Country()
# c.available_films.all()