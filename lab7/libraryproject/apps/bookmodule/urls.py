from django.urls import include, path
from . import views

urlpatterns = [
    # path('', views.index),
    path('index2/<int:val1>/', views.index2),
    # path('<int:bookId>', views.viewBook),
    
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),

    path('html5/', include('apps.bookmodule.html5_urls')),
    
    #lab6
    path('search/', views.search, name="books.search"),

    
]