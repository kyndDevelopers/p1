from django.shortcuts import render
from django.http import HttpResponse
from tools.models import topToolbar
# Create your views here.

def index(request):
    toolbar_data = topToolbar.objects.first()
    return render(request, "pages/index.html", {'toolbar_data': toolbar_data})

def about(request):
    toolbar_data = topToolbar.objects.first()
    return render(request, "pages/about.html", {'toolbar_data': toolbar_data})

def services(request):
    toolbar_data = topToolbar.objects.first()
    return render(request, "pages/services.html", {'toolbar_data': toolbar_data})