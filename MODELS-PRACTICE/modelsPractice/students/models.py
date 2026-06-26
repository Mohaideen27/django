from django.db import models

# Create your models here.
class studentDetails(models.Model):
    name=models.CharField()
    rNo=models.IntegerField()
    course=models.CharField()