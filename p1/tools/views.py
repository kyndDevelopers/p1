from django.shortcuts import render
from .models import topToolbar

# Create your views here.
def header_view(request):
    toolbar_data = topToolbar.objects.first()
    return render(request, 'toolbar.html', {'toolbar_data': toolbar_data})