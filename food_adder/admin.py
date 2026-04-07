from django.contrib import admin

# Register your models here.
from .models import Food
from .models import Meal_Item
from .models import Meal

admin.site.register(Food)
admin.site.register(Meal_Item)
admin.site.register(Meal)