from pyexpat import model
# from tkinter import CASCADE
from django.db import models



# Create your models here.



class Cohort(models.Model):
    number = models.IntegerField(default=0, unique=True)
    name = models.CharField(max_length=20, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
 

GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others'),
)  


class Native(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER, default='others')
    number = models.CharField(default=0, max_length=20, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    birthday = models.DateField()



    def __str__(self):
        return self.first_name + self.last_name

