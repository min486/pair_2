from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
# Create your views here.


def index(request):
    reviews = Review.objects.all()
    
    return render(request, 'movies/index.html', {"reviews":reviews})

def detail(request, pk):
    review = Review.objects.get(pk=pk)

    return render(request, 'movies/detail.html', {"review":review})

def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save()
            return redirect('movies:detail', pk=new_review.id)
    else:
        review_form = ReviewForm()
    return render(request, 'movies/create.html', {'review_form':review_form})

def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            new_review = review_form.save()
            return redirect('movies:detail', pk=new_review.id)
    else:
        review_form = ReviewForm(instance=review)
    return render(request, 'movies/create.html', {'review_form':review_form})

def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('movies:index')