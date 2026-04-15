from django.shortcuts import render
from django.http import HttpResponse
from .models import Food
from .models import Meal_Item
from .models import Meal
from .models import Food_Data
from .models import Meal_contents
from django.template import loader
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/accounts/login/")
def my_hello(request):
    Meals=Meal.objects.filter(Q(user_id=request.user.id)).values()
    L2=len(Meals)
    c2=0
    array=[]
    while c2<L2:
        array.append(Meals[c2]["name"])
        c2=c2+1
    if request.method=="POST" and request.POST.get("meal_name") not in array and len(request.POST.getlist("action"))==0:
        # getlist function was found looking at an AI and used to get the items in a meal that had just been created
        # to help save information to the database
        L=len(request.POST.getlist("example"))
        c=0
        # information on dictionaries from w3schools no longer used
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
            # getlist function was found looking at an AI and used to get the items in a meal that had just been created
            # to help save information to the database
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
        #
        food_list=[]
        food_list.append(5526)
        Meals=Meal.objects.filter(Q(user_id=request.user.id)).values()
        food_datas=Food_Data.objects.filter(id__in=food_list).values()
        #
        meal_contents0=Meal_contents()
        meal_contents0.meal=meal.name
        meal_contents0.potassium=meal_item.mass*food_datas[0]["potassium"]/100000
        meal_contents0.calcium=meal_item.mass*food_datas[0]["calcium"]/100000
        meal_contents0.magnesium=meal_item.mass*food_datas[0]["magnesium"]/100000
        meal_contents0.sodium=meal_item.mass*food_datas[0]["sodium"]/100000
        meal_contents0.energy_kcal=meal_item.mass*food_datas[0]["energy_kcal"]/100
        meal_contents0.save()
        meal_contents=Meal_contents.objects.all().values()
        context={
            'user_id':request.user.id,
            'Meals':Meals,
            'meal_items':meal_items,
            'item_count':item_count,
            'food_data':food_datas,
            'meal_contents':meal_contents,
        }
        #template = loader.get_template('meal_edit.html')
        #return HttpResponse(template.render(context,request))
        # information on passing context into a webpage found on w3schools
        return render(
           request,
           "meal_edit.html",
           context
        )
    else:
        foods=Food.objects.all().values()
        meals=Meal.objects.all().values()
        context = {
            "foods":foods,
            "meals":meals,
        }
        # information on passing context into a webpage found on w3schools
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
        # information on passing context into a webpage found on w3schools
        foods=Food.objects.all().values()
        context = {
            "foods":foods
        }
        return render(
            request,
            "food_add.html",
            context
        )
def my_view_name(request):
    if request.method=="POST":
        foods=Food.objects.all().values()
        meals=Meal.objects.all().values()
        context = {
            "foods":foods,
            "meals":meals,
        }
        # information on passing context into a webpage found on w3schools
        return render(
            request,
            "food_add.html",
            context
        )
    
def meal_list(request):
    meal_results = Meal.objects.filter(Q(user_id=request.user.id)).values().order_by("id")
    context = {
        'meal_results': meal_results,
    }
    template = loader.get_template('meal_list.html')
    return HttpResponse(template.render(context, request))