from django.shortcuts import render
from .models import Project
from slider.models import CmsSlider

# Create your views here.
def home(request):
    slider_list = CmsSlider.objects.all()
    projects = Project.objects.all()
    dict_obj = {'slider_list' : slider_list,
                'projects': projects,
                }
    return render(request,'./home.html', dict_obj)
