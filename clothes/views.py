from django.shortcuts import render
from .models import Clothes

def homepage(request):
  clothes = Clothes.objects.all()
  context_menu = {
    'clothes':clothes
  }
  return render(request,'home.html',context_menu)

# Create your views here.
