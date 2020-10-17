from django.shortcuts import render
from .models import Proyecto
# Create your views here.


def portafolio(request):
    projects = Proyecto.objects.all()
    return render(request, "portfoli/portafolio.html",{'projects':projects})