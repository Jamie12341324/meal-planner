from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Food(models.Model):
    name = models.CharField(max_length=255)
    featured_image = CloudinaryField('image', default='placeholder')

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="meal_username")
    name = models.CharField(max_length=255)

class Meal_Item(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="meal_name")
    food_code=models.CharField(max_length=20)
    mass=models.IntegerField(null=True) 

class Food_Data(models.Model):
   food_code = models.CharField(max_length=20)
   food_name = models.CharField(max_length=100)
   food_group = models.CharField(max_length=20)
   water = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   protein = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   fat = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   carbohydrate = models.DecimalField(null=True, max_digits=6, decimal_places=1) 
   energy_kcal = models.IntegerField(null=True) 
   starch= models.DecimalField(null=True, max_digits=6, decimal_places=1)
   total_sugars = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   glucose = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   galactose = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   fructose = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   sucrose = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   maltose = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   lactose = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   alcohol = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   nsp = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   aoac_fibre = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   cholesterol = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   sodium = models.IntegerField(null=True)
   potassium = models.IntegerField(null=True)
   calcium = models.IntegerField(null=True)
   magnesium = models.IntegerField(null=True)
   phosphorus = models.IntegerField(null=True)
   iron = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   copper = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   zinc = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   chloride = models.IntegerField(null=True)
   manganese = models.DecimalField(null=True, max_digits=6, decimal_places=1)
   selenium = models.IntegerField(null=True)
   iodine = models.IntegerField(null=True)
   retinol = models.IntegerField(null=True)
   carotene = models.IntegerField(null=True) 
   retinol_equivalent = models.IntegerField(null=True)
   vitamin_d = models.IntegerField(null=True)
   vitamin_e = models.IntegerField(null=True)
   vitamin_k1 = models.IntegerField(null=True)
   thiamin = models.IntegerField(null=True)
   riboflavin = models.IntegerField(null=True)
   miacin = models.IntegerField(null=True)
   tryptophan = models.IntegerField(null=True)
   niacin_equivalent = models.IntegerField(null=True)
   vitamin_b6 = models.IntegerField(null=True)
   vitamin_b12 = models.IntegerField(null=True)
   folate = models.IntegerField(null=True)
   pantothenate = models.IntegerField(null=True)
   biotin = models.IntegerField(null=True)
   vitamin_c = models.IntegerField(null=True)
   food_name_lcase = models.CharField(max_length=100, null=True)

def __str__(self):
    return f"{self.food_code} {self.food_name}"
