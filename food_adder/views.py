from django.shortcuts import render
from django.http import HttpResponse
from .models import Food
# Create your views here.

def my_hello(request):
    foods=Food.objects.all().values()
    context = {
        "foods":foods
    }
    return render(
        request,
        "food_add.html",
        context
    )
    # return HttpResponse("Hello, blog!!")