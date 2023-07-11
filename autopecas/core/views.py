from django.shortcuts import render

from item.models import category, Item

def index(request):
    items = Item.objects.filter(foi_vendido=False) [0:6]
    categorias = category.objects.all()

    return render(request, 'core/index.html', {
        'categorias': categorias,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')
