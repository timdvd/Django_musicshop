from django.urls import path, include
from .views import SearchListView


urlpatterns = [
    path('results/', SearchListView.as_view(), name='search'),
]