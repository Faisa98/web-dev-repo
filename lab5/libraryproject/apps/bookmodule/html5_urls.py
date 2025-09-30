from django.urls import path
from . import views

urlpatterns = [
    
    path('links', views.links, name="books.links"),
    path('text/formatting', views.text, name="books.text"),
    path('listing', views.listing, name="books.listing"),
    path('tables', views.tables, name="books.tables"),
    
]