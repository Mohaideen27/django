from django.shortcuts import render
from .models import Company
from .forms import CompanyForm
# Create your views here.
def company_register(request):
    if request.method=='POST':
        form=CompanyForm(request.POST)
        if  form.is_valid:
                company_name=form.changed_data('company_name')
                email=form.changed_data('email')
                phone=form.changed_data('phone')
                location=form.changed_data('location')
                website=form.changed_data('website')
                description=form.changed_data('description')
                Company.objects.create(
                     
                )
    else:
        form=CompanyForm()
    return render(request, 'compay_register.html',{'form':'form'})