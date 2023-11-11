from django.shortcuts import render, redirect
from .forms import TeachersClassForm
# Create your views here.
import json 
from . import views
from .models import TeachersClass
def index(request) :
    return render(request,'app/index.html')


def classes(request) :
    return render(request,'app/classes.html')

def add_teachers_class(request):
    if request.method == 'POST':
        form = TeachersClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a view displaying all classes
    else:
        form = TeachersClassForm()
    return render(request, 'app/add_teachers_class.html', {'form': form})


def view_model_entries(request):
    entries = TeachersClass.objects.all()  # Query all entries in MyModel
    return render(request, 'app/model_entries.html', {'entries': entries})

def single_class(request) :
    return render(request, 'app/single_class.html')
