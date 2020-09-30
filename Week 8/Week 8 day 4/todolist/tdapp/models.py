from django.db import models
import datetime

# Create your models here.

class User(models.Model): 
    username = models.CharField(max_length= 30)
    password = models.CharField(max_length= 30)

class Todo(models.Model):
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    title= models.CharField(max_length= 30)
    details= models.CharField(max_length= 100)
    has_been_done : models.BooleanField(default= False)
    date_creation : models.DateField(default=datetime.date.today)
    date_completion: models.DateField()
    deadline_date: models.DateField()
# This model has a One to Many relationship with the User Model : A User can have many todo, but a todo belongs to only one user.

class Category(models.Model):
    name= models.CharField(max_length= 30)
    image= models.URLField()
# This model has a Many to Many relationship with the Todo Model : A Todo can have many cqtegories, and a category can be shared among many todos.
# Example of category : work, home, shopping, studies, social

