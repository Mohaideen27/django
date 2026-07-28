from django.forms import ModelForm
from .models import Candidates
class CandidateForm(ModelForm):
    class Meta:
        model=Candidates
        fields='__all__'