from django.shortcuts import render
from .models import Book, Student

# def index(request):
#     name = request.GET.get("name") or "world!"
#     return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1 = 0):
    return render(request, "bookmodule/index2.html", {"val1": val1})

def viewBook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)

def index(request):
    return render(request, "bookmodule/index.html")
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, 'bookmodule/links.html')
def text(request):
    return render(request, 'bookmodule/text.html')
def listing(request):
    return render(request, 'bookmodule/listing.html')
def tables(request):
    return render(request, 'bookmodule/tables.html')

# lab6
def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

# lab7
def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/booklist.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull =False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/booklist.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
#lab8
from django.db.models import Q

def task1(request):
    mybooks=Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/booklist.html', {'books':mybooks})
def task2(request):
    mybooks=Book.objects.filter(Q(edition__gt=3) & (Q(title__contains = 'qu') | Q(author__contains = 'qu')))
    return render(request, 'bookmodule/booklist.html', {'books':mybooks})
def task3(request):
    mybooks=Book.objects.filter(~Q(edition__gt=3) & (~Q(title__contains = 'qu') | ~Q(author__contains = 'qu')))
    return render(request, 'bookmodule/booklist.html', {'books':mybooks})
def task4(request):
    mybooks=Book.objects.filter(~Q(edition__lte=0)).order_by('title')
    return render(request, 'bookmodule/booklist.html', {'books':mybooks})

from django.db.models import Count, Min, Max, Sum, Avg
def task5(request):
    agg1= Count('price')
    agg2= Sum('price', default=0)
    agg3= Avg('price', default=0)
    agg4= Max('price', default=0)
    agg5= Min('price', default=0)
    query=Book.objects.aggregate(co=agg1, to=agg2, av=agg3, ma=agg4, mi=agg5)
    return render(request, 'bookmodule/agg.html', {'query':query})

from django.db.models import Count
from .models import Address
def task7(request):
    data= Address.objects.annotate(numStu=Count('student'))
    return render(request, 'bookmodule/stuCity.html',{'data':data})

# lab 11
def lab11(request):
    return render(request, 'bookmodule/lab11.html', {'students': Student.objects.all()})