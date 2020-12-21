from django.shortcuts import render
from products.models import Product
from publishers.models import Publisher

def home(request):
    context = {
        'title': 'Home',
        'arrivals': Product.objects.all().filter(category='arrival').filter(active=True)[:10],
        'albums': Product.objects.all().filter(category='album').filter(active=True)[:10],
        'publishers': Publisher.objects.all().filter(active=True),
    }
    return render(request, 'home.html', context=context)

def portfolio(request):
    context = {
        'title': 'Portfolio',
    }
    return render(request, 'portfolio.html', context=context)