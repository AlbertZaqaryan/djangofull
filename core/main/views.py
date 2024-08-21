from django.shortcuts import render
from .models import Category, Product
# Create your views here.

def index(request):
    category_list = Category.objects.all()
    return render(request, 'index.html', context={
        'category_list':category_list
    })