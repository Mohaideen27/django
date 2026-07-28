from django.db import models
from candidates.models import Candidates
from jobs.models import Job

# Create your models here.
class Application(models.Model):
    candidates=models.ForeignKey(Candidates,on_delete=models.CASCADE)
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    applied_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=[('Applied','Applied'),
                                     ('Short Listed','Short Listed'),
                                     ('Rejected','Rejected'),
                                     ('On board','On board'),
                                     ('Selected','Selected')])
    def __str__(self):
        return f"name:{self.candidates.name} job title:{self.job.title}"