from django.shortcuts import render
from django.http import HttpResponse
from .models import Food
from .models import Meal_Item
from .models import Meal
from django.template import loader
from django.db.models import Q
# Create your views here.

def my_hello(request):
    if request.method=="POST":
        L=len(request.POST.getlist("example"))
        c=0
        # meal_items=Meal_Item.objects.all().values()
        # L2=len(meal_items)
        # highest=0
        # c3=0
        # while c3<L2:
        #     print("meal_items[c3]",meal_items[c3])
        #     if meal_items[c3]["meal_id"]>highest:
        #         highest=meal_items[c3]["meal_id"]
        #     c3=c3+1
        meal=Meal()
        meal.name=request.POST.get("meal_name")
        meal.user = request.user
        meal.save()
        while c<L:
            meal_item=Meal_Item()
            meal_item.food_code=request.POST.getlist("example")[c]
            meal_item.mass=100
            meal_item.meal=meal
            #meal_item.meal.name=request.POST.get("meal_name")
            #meal_item.meal_id=highest+1
            #print("highest",highest)
            meal_item.save()
            c=c+1
        meal_items=Meal_Item.objects.filter(Q(meal__user_id=request.user.id)).values()
        item_count = meal_items.count
        Meals=Meal.objects.filter(Q(user_id=request.user.id)).values()
        context={
            'user_id':request.user.id,
            'Meals':Meals,
            'meal_items':meal_items,
            'item_count':item_count,
        }
        #template = loader.get_template('meal_edit.html')
        #return HttpResponse(template.render(context,request))
        return render(
           request,
           "meal_edit.html",
           context
        )
    else:
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
def start_meal(request):
    if request.method=="POST":
        meal_item=Meal_Item()
        meal_item.food_code=request.POST.getlist["example"]
        meal_item.mass=100
        meal_item.save()
    else:
        foods=Food.objects.all().values()
        context = {
            "foods":foods
        }
        return render(
            request,
            "food_add.html",
            context
        )