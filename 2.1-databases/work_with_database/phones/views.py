from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', None)
    phones = [i for i in Phone.objects.all()]
    if sort == 'name':
        phones.sort(key=lambda x: x.name)
    elif sort == 'min_price':
        phones.sort(key=lambda x: x.price)
    elif sort == 'max_price':
        phones.sort(key=lambda x: x.price, reverse=True)
    return render(request, template, context={'phones': phones})


def show_product(request, slug):
    template = 'product.html'
    model = get_object_or_404(Phone, slug=slug)
    return render(request, template, context={'phone': model})
