from django.db import models
class student(models.Model):
    name=models.CharField(max_length=20)
    rNo=models.IntegerField()
    age=models.IntegerField()
    email=models.IntegerField()
    dob=models.DateField()

