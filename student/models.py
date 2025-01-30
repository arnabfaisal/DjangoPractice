from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    coursesTaken=models.ManyToManyField(Course)

    def __str__(self):
        return self.name
    

