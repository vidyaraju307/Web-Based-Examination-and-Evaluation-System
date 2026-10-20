from django.db import models

class Registration(models.Model):
    name=models.CharField(max_length=200)
    regnumber=models.CharField(max_length=6)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    course=models.CharField(max_length=100)
    semester=models.CharField(max_length=10)
    password=models.CharField(max_length=200)
    


