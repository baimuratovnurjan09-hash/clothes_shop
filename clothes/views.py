from django.shortcuts import render
from .models import Clothes

def homepage(request):
    query = request.GET.get('q')  # Получаем текст из поискового поля
    if query:
        clothes = Clothes.objects.filter(title__icontains=query)
    else:
        clothes = Clothes.objects.all()

    context_menu = {
        'clothes': clothes,
        'query': query,
    }
    return render(request, 'home.html', context_menu)
# Create your views here.
