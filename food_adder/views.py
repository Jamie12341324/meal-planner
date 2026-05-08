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
from django.shortcuts import redirect

# Create your views here.

@login_required(login_url="/accounts/login/")
# my_hello
# by default render the food_add page and if the method is POST render the meal update page
def my_hello(request,id):
    code_to_name={
        "Strawberry":"14-324",
        "Banana":"14-318",
        "Apple":"14-319",
        "Orange":"14-360",
        "Grapes":"14-323",
        "Raspberries":"14-375",
    }
    Meals=Meal.objects.filter(Q(user_id=request.user.id)).values()
    L2=len(Meals)
    c2=0
    array=[]
    while c2<L2:
        array.append(Meals[c2]["name"])
        c2=c2+1

    if request.method=="POST":
        c = 0
        L=len(request.POST.getlist("example"))
        
        while c<L:
            data_code = code_to_name[ request.POST.getlist("example")[c] ]
            meal_chk = Meal_Item.objects.filter(Q(meal_id=id) & Q( food_id = data_code )  ).values()
            if meal_chk.count() < 1:
                meal_item=Meal_Item()
                meal_item.food_code=request.POST.getlist("example")[c]
                meal_item.mass=100
                meal_item.meal_id = id
                meal_item.food_id = code_to_name[ request.POST.getlist("example")[c] ] 
                meal_item.save()
            c=c+1

        return redirect("/meal_update/"+str(id))
    else:
        foods=Food.objects.all().values()
        meals=Meal.objects.all().values()
        meal=Meal.objects.get(id=id)
        meal_name = meal.name
        context = {
            "foods":foods,
            "meals":meals,
            "meal_name":meal_name,
        }
        # information on passing context into a webpage found on w3schools
        return render(
            request,
            "food_add.html",
            context
        )
    

@login_required(login_url="/accounts/login/")
# meal_list
# renders the meal list page
def meal_list(request):
    meal_results = Meal.objects.filter(Q(user_id=request.user.id)).values().order_by("id")
    context = {
        'meal_results': meal_results,
    }
    template = loader.get_template('meal_list.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url="/accounts/login/")
# meal_update
# renders the meal update page
def meal_update(request,id):
    meal = Meal.objects.get(id=id)
    meal_name = meal.name
    meal_id = meal.id
    if request.method == "POST":
        masses=request.POST.getlist("mass")
        meal_items = Meal_Item.objects.filter(Q(meal_id=id)).values()
        for item in meal_items:
            meal_item = Meal_Item.objects.get(id=item["id"])
            mass = int(request.POST['mass' + str(item["id"]) ])
            meal_item.mass = mass
            meal_item.save() 
        return redirect("/meal_update/"+str(id))
    else:
        # This query uses the food foreign key to access the food data using the __ (double underline) convention
        item_list = Meal_Item.objects.filter(Q(meal__user_id=request.user.id) and Q(meal_id=id)).values('id','food__food_name','mass','food__potassium','food__calcium','food__magnesium','food__sodium','food__energy_kcal')

        potassium = 0
        calcium = 0
        magnesium = 0
        sodium = 0
        energy_kcal = 0

        for item in item_list:
            potassium =  potassium + item['mass'] * item['food__potassium'] / 100000
            calcium = calcium + item['mass'] * item['food__calcium'] / 100000
            magnesium = magnesium + item['mass'] * item['food__magnesium'] / 100000
            sodium = sodium + item['mass'] * item['food__sodium'] / 100000
            energy_kcal = energy_kcal + item['mass'] * item['food__energy_kcal'] / 100000
            
        context = {
        "meal_name": meal_name,
        "meal_id": meal_id,
        "item_list": item_list,
        "potassium": potassium,
        "calcium": calcium,
        "magnesium": magnesium,
        "sodium": sodium,
        "energy_kcal": energy_kcal,
    }
    template = loader.get_template('meal_update.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url="/accounts/login/")
# meal_delete
# deletes a meal and then goes back to the meal list page
def meal_delete(request,id):
    Meal.objects.filter(Q(user_id=request.user.id) & Q(id=id)).delete()
    return redirect("/meal_list")

@login_required(login_url="/accounts/login/")
# meal_item_delete
# deletes a meal item then renders th email update page
def meal_item_delete(request,meal_id,meal_item_id):
    Meal_Item.objects.filter(Q(id=meal_item_id) & Q(meal_id=meal_id)).delete()
    return redirect("/meal_update/"+str(meal_id))

@login_required(login_url="/accounts/login/")
# meal_create
# returns you back to the same page (meal_create) if you have not given a name to create a meal with or
# a meal with that name already exists
# if you have given a meal name then it is saved and you are sent to the meal list page
def meal_create(request):
    if request.method == "POST":
        if request.POST["meal_name"] == '':
            return redirect("/meal_create/")
        meal_records = Meal.objects.filter(Q(name=request.POST["meal_name"]) & Q(user_id=request.user.id)).values()
        if not meal_records.exists():
            meal=Meal()
            meal.user_id=request.user.id
            meal.name=request.POST["meal_name"]
            meal.save()
            return redirect("/meal_list/")
        else:
            return redirect("/meal_create/")
    else:
        meals=Meal.objects.all().values()
        context={"meals":meals,}
        return render(
            request,
            "meal_create.html",
            context
        )
    
@login_required(login_url="/accounts/login/")
# meal_create2
# does a similar job to meal_create but it is for renaming a meal instead of creating one
# returns you back to the same page (meal_create2) if you have not given a name to rename a meal with or
# a meal with that name already exists
# if you have given a meal name then it is saved and you are sent to the meal list page
def meal_create2(request,meal_id):
    meals=Meal.objects.all().values()
    meal=Meal.objects.get(id=meal_id)
    meal_name=meal.name
    if request.method == "POST":
        if request.POST["meal_name"] == '':
            return redirect("/meal_create2/"+str(meal_id))
        meal_records = Meal.objects.filter(Q(name=request.POST["meal_name"]) & Q(user_id=request.user.id)).values()
        if meal_records.exists():
            return redirect("/meal_create2/"+str(meal_id))
        meal.name=request.POST["meal_name"]
        meal.save()
        return redirect("/meal_list/")
    else:
        named=True
        context={"meal_name": meal_name,
                 "named": named,
                 "meals": meals,}
        return render(
            request,
            "meal_create.html",
            context
        )