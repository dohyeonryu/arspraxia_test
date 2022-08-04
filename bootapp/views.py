from django.shortcuts import render
from .models import Category

# Create your views here.

def home(request):
        cate=Category.objects.all()
	return render(request, 'home.html',{"cate":cate})


def about(request):
    return render(request, 'about.html')
