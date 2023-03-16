from django.http import JsonResponse
from django.shortcuts import render
from . import helper_functions


revs = helper_functions.load_reviews()


def home(request):
    reviews = helper_functions.sort_reviews(revs, True, 1, True, 1)
    context ={
        "reviews": reviews,
    }
    return render(request, 'review_filter/index.html', context)


def send(request):
    rating = int(request.POST['rating'])
    min_rating = int(request.POST['min_rating'])
    date = int(request.POST['date'])
    prioritize = int(request.POST['prioritize'])

    reviews = helper_functions.sort_reviews(revs, rating, min_rating, date, prioritize)
    return JsonResponse({"reviews": reviews})
