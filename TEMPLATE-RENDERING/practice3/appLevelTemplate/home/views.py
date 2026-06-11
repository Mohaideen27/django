from django.shortcuts import render

# Create your views here.
def home(request):
    context={
        'place1' : "Chennai (Tamil Nadu)",
        'place2':"Bangalore (Karnataka)",
          'place3':'Hyderabad (Telangana)',
          'place4':'Kochi (Kerala)',
          'place5':'Ooty & Kodaikanal',
          'place6':'Mysore & Hampi',
          'place7':'Munnar & Alleppey',
          'place8':'Visakhapatnam & Tirupati',
          'place9':'Pondicherry (UT)',
          'place0':'Wayanad & Coorg',
    }
    return render(request, 'home.html',context)