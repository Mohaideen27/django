from django.db import models

# Create your models here.
class Company(models.Model):
    company_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=14)
    location=models.CharField(max_length=100)
    website=models.URLField(null=True, max_length=50)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
