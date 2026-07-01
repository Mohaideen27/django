from django.db import models

# Create your models here.
class AccInfo(models.Model):
    name =models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    dob = models.DateField(null=True)
    course = models.CharField(max_length=100)
    yop=models.IntegerField(null=True)

    def __str__(self):
        return self.name