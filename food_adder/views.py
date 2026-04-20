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
def my_hello(request,id):
    code_to_name={
        "Strawberry":"14-324",
        "Banana":"14-318",
        "Apple":"14-319",
        "Orange":"14-360",
    }
    Meals=Meal.objects.filter(Q(user_id=request.user.id)).values()
    #Meals=Meal.objects.filter(Q(user_id=request.user.id) & Q(id=id) ).values()
    
    L2=len(Meals)
    c2=0
    array=[]
    while c2<L2:
        array.append(Meals[c2]["name"])
        c2=c2+1

    if request.method=="POST":
        print(request.POST.getlist("example"))
        c = 0
        L=len(request.POST.getlist("example"))
        
        while c<L:
            #print(request.POST.getlist("example")[c] + " " + code_to_name[ request.POST.getlist("example")[c] ] )
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
    
    
    
        meal_items=Meal_Item.objects.filter(Q(meal_id=id)).values()
        #if request.method=="POST" and request.POST.get("meal_name") in array and len(request.POST.getlist("action"))==0:
        # getlist function was found looking at an AI and used to get the items in a meal that had just been created
        # to help save information to the database
        L=len(request.POST.getlist("example"))
        print(request.POST.getlist("example"))
        #L=len(code_to_name)
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
        meal_items=Meal_Item.objects.filter(Q(meal_id=id)).values()
        #     c3=c3+1

        #meal=Meal()
        #meal = Meal.objects.filter(Q(id=id)).values()
        #meal.name=request.POST.get("meal_name")
        #meal.name="fruit3"
        #meal.user = request.user
        #meal.save()
        #meal_name = meal.name

        meal = Meal.objects.get(id=id)
        c=0
        while c<L:
            do=False
            for meal2 in meal_items:
                if request.POST.getlist("example")[c] == meal2["food_code"]:
                    do=True
                print("meal2[food_code]",meal2["food_code"])
                print("request.POST.getlist(example)[c]",request.POST.getlist("example")[c])
                print("do",do)
            #if do==False:
                meal_item=Meal_Item()
                # getlist function was found looking at an AI and used to get the items in a meal that had just been created
                # to help save information to the database
                print("code" + str(c))
                meal_item.food_code=request.POST.getlist("example")[c]
                meal_item.mass=100
                meal_item.meal = meal
                meal_item.food_code_id = code_to_name[meal_item.food_code] 
                # meal_item.food_data_code_id = code_to_name[meal_item.food_code]
                #meal_item.meal.name=request.POST.get("meal_name")
                #meal_item.meal_id=highest+1
                #print("highest",highest)
                meal_item.save()
                print("meal_item.food_code",meal_item.food_code)
            c=c+1
        print("back to meal update")
        return redirect("/meal_update/"+str(id))

        meal_items=Meal_Item.objects.filter(Q(meal__user_id=request.user.id) and Q(meal_id=id)).values()
        item_count = meal_items.count
        #
        food_list=[]
        for item in meal_items:
            food_list.append(code_to_name[item['food_code']])
        Meals=Meal.objects.filter(Q(user_id=request.user.id)).values()
        food_datas=Food_Data.objects.filter(food_code__in=food_list).values()
        #
        meal_contents0=Meal_contents()
        c=0

        potassium = 0
        calcium = 0
        magnesium = 0
        sodium = 0
        energy_kcal = 0
        item_list = Meal_Item.objects.filter(Q(meal__user_id=request.user.id) and Q(meal_id=id)).values('id','mass','food__potassium','food__calcium','food__magnesium','food__sodium','food__energy_kcal')
        for item in item_list:
            potassium =  potassium + item['mass'] * item['food__potassium']
            calcium = calcium + item['mass'] * item['food__calcium']
            magnesium = magnesium + item['mass'] * item['food__magnesium']
            sodium = sodium + item['mass'] * item['food__sodium']
            energy_kcal = energy_kcal + item['mass'] * item['food__energy_kcal']
            
        meal_contents0.meal  =meal.name
        meal_contents0.potassium = potassium
        meal_contents0.calcium = calcium
        meal_contents0.magnesium = magnesium
        meal_contents0.sodium = sodium
        meal_contents0.energy_kcal = energy_kcal
        meal_contents0.save()
        meal_contents=Meal_contents.objects.all().values()

        #while c<L2:
        #    meal_contents0.meal=meal.name
        #    meal_contents0.potassium=meal_items[c].mass*food_datas[c]["potassium"]/100000
        #    meal_contents0.calcium=meal_items[c].mass*food_datas[c]["calcium"]/100000
        #    meal_contents0.magnesium=meal_items[c].mass*food_datas[c]["magnesium"]/100000
        #    meal_contents0.sodium=meal_items[c].mass*food_datas[c]["sodium"]/100000
        #    meal_contents0.energy_kcal=meal_items[c].mass*food_datas[c]["energy_kcal"]/100
        #    c=c+1
        #meal_contents0.save()
        #meal_contents=Meal_contents.objects.all().values()
        context={
            'meal_name':meal_name,
            'user_id':request.user.id,
            'Meals':Meals,
            'meal_items':meal_items,
            'item_count':item_count,
            'food_data':food_datas,
            'meal_contents':meal_contents0,
        }
        return redirect("/meal_update/"+str(id))
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

@login_required(login_url="/accounts/login/")
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
    
@login_required(login_url="/accounts/login/")
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
    
@login_required(login_url="/accounts/login/")
def meal_list(request):
    meal_results = Meal.objects.filter(Q(user_id=request.user.id)).values().order_by("id")
    context = {
        'meal_results': meal_results,
    }
    template = loader.get_template('meal_list.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url="/accounts/login/")
def meal_update(request,id):
    meal = Meal.objects.get(id=id)
    meal_name = meal.name
    meal_id = meal.id
    if request.method == "POST":
        masses=request.POST.getlist("mass")
        #m_id=masses[0].id[4:len(masses.id)]
        #print("thing",m_id)
        meal_items = Meal_Item.objects.filter(Q(meal_id=id)).values()
        for item in meal_items:
            meal_item = Meal_Item.objects.get(id=item["id"])
            mass = int(request.POST['mass' + str(item["id"]) ])
            meal_item.mass = mass
            meal_item.save() 
        #item2.save()
        #for masses2 in item2:
        #    meal_item.id=str(masses2.id)
        #    meal_item = Meal_Item.objects.get(id=meal_item.id)
        #    meal_item.mass = 50
        #    meal_item.save()
            #masses2['mass']=50
            #masses2.save()
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
        #"meal_items": meal_items,
    }
    template = loader.get_template('meal_update.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url="/accounts/login/")
def meal_delete(request,id):
    Meal.objects.filter(Q(user_id=request.user.id) & Q(id=id)).delete()
    return redirect("/meal_list")

@login_required(login_url="/accounts/login/")
def meal_item_delete(request,meal_id,meal_item_id):
    Meal_Item.objects.filter(Q(id=meal_item_id) & Q(meal_id=meal_id)).delete()
    return redirect("/meal_update/"+str(meal_id))