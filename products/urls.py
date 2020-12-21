from django.urls import path, include
from .views import ProductSlugView, AlbumsListView, ArrivalsListView, AddReview

urlpatterns = [
    path('product/<slug:slug>/', ProductSlugView.as_view(), name='product_detail'),
    path('arrivals/', ArrivalsListView.as_view(), name='all_arrivals'),
    path('albums/', AlbumsListView.as_view(), name='all_albums'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
]