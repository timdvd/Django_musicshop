from django.shortcuts import render, get_object_or_404
from .models import Publisher
from products.models import Product
from .models import Publisher
from django.views.generic import ListView
# Create your views here.

class PublisherWorkListView(ListView):
    model = Product
    template_name = 'publishers/publisher_works.html'
    context_object_name = 'works'
    ordering = ['-timestamp']
    paginate_by = 6

    def get_queryset(self):
        publisher = get_object_or_404(Publisher, name=self.kwargs.get('name'))
        return Product.objects.filter(author=publisher).order_by('-timestamp')

    def get_context_data(self, *args, **kwargs):
        context = super(PublisherWorkListView, self).get_context_data(*args, **kwargs)
        slug = self.kwargs.get('slug')
        context['title'] = 'Publisher Works'
        context['pubname'] = self.kwargs.get('name')
        return context
