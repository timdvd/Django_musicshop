from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
# Create your views here.

class SearchListView(ListView):
    template_name = 'search/result.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)
        else:
            return Product.objects.none()

    def get_context_data(self, *args, **kwargs):
        context = super(SearchListView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context
