#You need to import the render function in order to call it
from django.shortcuts import render
from persons.models import Person


   
def indexPageView(request) :
    return render(request, 'persons/index.html')

def dataPageView(request) :
    records = Person.objects.all()
    context = {
    "data" : records
    }
    return render(request, 'persons/data.html', context) 

def infoPageView(request, person_id):
    fields = Person.objects.get(id = person_id)
    context2 = {
        "data" : fields
    }
    return render(request, 'persons/info.html', context2) 