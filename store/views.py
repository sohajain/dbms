from django.shortcuts import render
from .models import book
# Create your views here.
def index(request):
    return render(request,'template.html')
def store(request):
    count=book.objects.all().count()
    context = {
        'count':count
    }
    return render(request,'store.html',context)
