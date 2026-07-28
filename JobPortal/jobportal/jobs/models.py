from django.db import models
from companies.models import Company

# Create your models here.
class Job(models.Model):
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    title=models.CharField()
    description=models.TextField()
    location=models.CharField()
    salary=models.DecimalField(max_digits=8,decimal_places=2)
    experience_required=models.PositiveIntegerField()
    jobtype=models.CharField(choices=[('Experienced','Experienced'),('Fresher','Fresher'),('Intern','Intern')])
    vacanies=models.PositiveIntegerField()
    deadline=models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title