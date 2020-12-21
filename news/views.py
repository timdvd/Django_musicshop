from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'news'
    ordering = ['-timestamp']
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(active=True).order_by('-timestamp')

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['title'] = 'News'
        return context
