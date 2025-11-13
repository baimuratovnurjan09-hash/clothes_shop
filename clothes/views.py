from django.shortcuts import render
from .models import Clothes

def homepage(request):
    query = request.GET.get('q') 
    if query:
        clothes = Clothes.objects.filter(title__icontains=query)
    else:
        clothes = Clothes.objects.all()

    context_menu = {
        'clothes': clothes,
        'query': query,
    }
    return render(request, 'home.html', context_menu)

def detail(request,id):
    clothes = Clothes.objects.filter(book_id=id)
    context = {'clothes':clothes}
    return render(request,'detail.html',context)
# Create your views here.
