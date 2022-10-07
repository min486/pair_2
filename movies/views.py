from django.shortcuts import render
from .models import Review
# Create your views here.


def index(request):
    reviews = Review.objects.all()
    
    return render(request, 'movies/index.html', {"reviews":reviews})

def detail(request, pk):
    review = Review.objects.get(pk=pk)

    return render(request, 'movies/detail.html', {"review":review})

