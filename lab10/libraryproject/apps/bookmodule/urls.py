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

    #lab7
    path('simple/query/', views.simple_query, name="books.simple_query"),
    path('complex/query/', views.complex_query, name="books.complex_query"),
    
    #lab10
    path('l10p1/listB/', views.l10_part1_listB, name="books.l10p1"),
    path('l10p1/addB/', views.l10_part1_addB, name="books.l10p1add"),
    path('l10p1/editB/<bID>', views.l10_part1_editB, name="books.l10p1edit"),
    path('l10p1/deleteB/<bID>', views.l10_part1_deleteB, name="books.l10p1delete"),

    path('l10p2/listB/', views.l10_part2_listB, name="books.l10p2"),
    path('l10p2/addB/', views.l10_part2_addB, name="books.l10p2add"),
    path('l10p2/editB/<bID>', views.l10_part2_editB, name="books.l10p2edit"),
    path('l10p2/deleteB/<bID>', views.l10_part2_deleteB, name="books.l10p2delete"),

]