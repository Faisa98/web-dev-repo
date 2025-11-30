from django.shortcuts import redirect, render

from apps.bookmodule import forms
from .models import Book

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

# lab10
def l10_part1_listB(request):
    return render(request, 'bookmodule/l10_part1.html', {'books': Book.objects.all()})

def l10_part1_addB(request):
    if request.method == "POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        edition=request.POST.get('edition')
        price=request.POST.get('price')

        object=Book(title=title, author=author, edition=edition, price=float(price))
        object.save()
        return redirect('books.l10p1')
    return render(request, 'bookmodule/l10_part1_add.html')

def l10_part1_editB(request, bID):
    book = Book.objects.get(id=bID)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.edition = request.POST.get('edition')
        book.price = float(request.POST.get('price'))
        book.save()
        return redirect('books.l10p1')
    return render(request, 'bookmodule/l10_part1_edit.html', {'book': book})

def l10_part1_deleteB(request, bID):
    book = Book.objects.get(id=bID)
    if request.method == "POST":
        book.delete()
    return redirect('books.l10p1')

# part 2
def l10_part2_listB(request):
    return render(request, 'bookmodule/l10_part2.html', {'books': Book.objects.all()})

def l10_part2_addB(request):
    if request.method == "POST":
        form = forms.AdditBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books.l10p2')
    else:
        form = forms.AdditBookForm(None)
    return render(request, 'bookmodule/l10_part2_add.html', {'form': form})

def l10_part2_editB(request, bID):
    book = Book.objects.get(id=bID)
    if request.method == "POST":
        form = forms.AdditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books.l10p2')
    else:
        form = forms.AdditBookForm(None, instance=book)
    return render(request, 'bookmodule/l10_part2_edit.html', {'form': form})

def l10_part2_deleteB(request, bID):
    book = Book.objects.get(id=bID)
    if request.method == "POST":
        form = forms.DeleteBookForm(request.POST)
        if form.is_valid():
            book.delete()
            return redirect('books.l10p2')
    else:
        form = forms.DeleteBookForm(None)
    return render(request, 'bookmodule/l10_part2_delete.html', {'form': form})