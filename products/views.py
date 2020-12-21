from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from products.models import Product
from carts.models import Cart
from django.http import Http404
# Create your views here.

class ArrivalsListView(ListView):
    model = Product
    template_name = 'products/arrivals.html'
    ordering = ['-timestamp']

    def get_context_data(self, *args, **kwargs):
        context = super(ArrivalsListView, self).get_context_data(*args, **kwargs)
        context['arrivals'] = Product.objects.all().filter(category='arrival')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().filter(category='arrival')

class AlbumsListView(ListView):
    model = Product
    template_name = 'products/albums.html'
    ordering = ['-timestamp']

    def get_context_data(self, *args, **kwargs):
        context = super(AlbumsListView, self).get_context_data(*args, **kwargs)
        context['albums'] = Product.objects.all().filter(category='album')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().filter(category='album')


class ProductSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        
        slug = self.kwargs.get('slug')
        prod_obj = Product.objects.get(slug=slug)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request =self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404('Not found')
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()

        return instance

class AddReview(View):
    """ Comments """
    def post(self, request, pk):
        return redirect('/')