from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import category,Item

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category',0)
    categorias = category.objects.all()
    items = Item.objects.filter(foi_vendido = False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains = query) | Q(Descrição__icontains = query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categorias': categorias,
        'category_id': int(category_id),
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category = item.category, foi_vendido = False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

