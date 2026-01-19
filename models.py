from django.db import models

class Student(models.Model):
    regno=models.IntegerField()
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)

