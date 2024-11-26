from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(models.Model):
    pass


class Faculty(models.Model):
    name = models.CharField(max_length=150)
    department = models.CharField(max_length=100, blank=True, null=True,)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    std_id = models.IntegerField()
    std_name = models.CharField(max_length=200)
    std_phone = models.CharField(max_length=20)
    std_parent = models.CharField(max_length=200)
    std_fuculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank=True, null=True, related_name="students")
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")


    
    def __str__(self):
        return self.std_id, self.std_name, self.std_phone, self.std_parent, self.std_fuculty