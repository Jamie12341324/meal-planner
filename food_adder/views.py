from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_hello(request):
    return render(
        request,
        "food_add.html"
    )
    # return HttpResponse("Hello, blog!!")