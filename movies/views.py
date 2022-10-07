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

def create(reqeust):
    if reqeust.method == 'POST':
        review_form = ReviewForm(reqeust.POST)
        if review_form.is_valid():
            new_review = review_form.save()
            return redirect('movies:detail', pk=new_review.id)
    else:
        review_form = ReviewForm()
    return render(reqeust, 'movies/create.html', {'review_form':review_form})