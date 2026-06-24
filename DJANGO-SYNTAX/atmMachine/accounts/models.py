from django.db import models

# Create your models here.
class accounts(models.Model):
    acName=models.CharField(max_length=50)
    acNum=models.IntegerField()
    acType=models.CharField(max_length=50)
    bal=models.FloatField()
    pin=models.IntegerField()

    def __str__(self):
        return self.acName