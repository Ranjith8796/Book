from django.shortcuts import redirect, render
from .models import bookform
from .filter import BookFilter



# Create your views here.
def home(request):
    return render(request,'bookinfo/index.html')

def Add(request):
    if request.method=='POST':
        bookname=request.POST['bookname']
        author=request.POST['author']
        genre=request.POST['genre']
        language=request.POST['language']
        bookf=bookform(bookname=bookname,author=author,genre=genre,language=language)           
        bookf.save()
        return redirect('/')

    return render(request,'bookinfo/bform.html')


def viewb(request):
    allbook=bookform.objects.all()
    myfilter=BookFilter(request.GET, queryset=bookform.objects.all())
    allbook= myfilter.qs
    
    
    
    return render(request,'bookinfo/filter.html', {'allbook':allbook,'myfilter':myfilter})