from django.db import models

# Create your models here.
class Candidates(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone_no=models.CharField(max_length=14)
    qualification=models.CharField(max_length=50)
    experience=models.IntegerField()
    skills=models.TextField()
    resume=models.FileField()
    profile_img=models.ImageField
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


