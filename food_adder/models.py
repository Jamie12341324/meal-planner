from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Food(models.Model):
    name = models.CharField(max_length=255)
    featured_image = CloudinaryField('image', default='placeholder')

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Meal_Item(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food_code=models.CharField(max_length=20)
    # food_data=models.ForeignKey(Food_Data, on_delete=models.CASCADE, related_name="Food_Data")
    # IntegerField from stackoverflow
    mass=models.IntegerField(null=True)
    
class Meal_contents(models.Model):
    meal=models.CharField(max_length=255)
    potassium=models.DecimalField(null=True, max_digits=11, decimal_places=2)
    calcium=models.DecimalField(null=True, max_digits=11, decimal_places=2)
    magnesium=models.DecimalField(null=True, max_digits=11, decimal_places=2)
    sodium = models.DecimalField(null=True, max_digits=11, decimal_places=2)
    energy_kcal = models.DecimalField(null=True, max_digits=11, decimal_places=2)

class Food_Data(models.Model):
   food_code = models.CharField(max_length=20)
   food_name = models.CharField(max_length=100)
   food_group = models.CharField(max_length=20)
   water = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   protein = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   fat = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   carbohydrate = models.DecimalField(null=True, max_digits=11, decimal_places=2) 
   energy_kcal = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   starch= models.DecimalField(null=True, max_digits=11, decimal_places=2)
   total_sugars = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   glucose = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   galactose = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   fructose = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   sucrose = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   maltose = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   lactose = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   alcohol = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   nsp = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   aoac_fibre = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   cholesterol = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   sodium = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   potassium = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   calcium = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   magnesium = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   phosphorus = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   iron = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   copper = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   zinc = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   chloride = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   manganese = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   selenium = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   iodine = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   retinol = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   carotene = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   retinol_equivalent = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   vitamin_d = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   vitamin_e = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   vitamin_k1 = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   thiamin = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   riboflavin = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   miacin = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   tryptophan = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   niacin_equivalent = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   vitamin_b6 = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   vitamin_b12 = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   folate = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   pantothenate = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   biotin = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   vitamin_c = models.DecimalField(null=True, max_digits=11, decimal_places=2)
   food_name_lcase = models.CharField(max_length=100, null=True)

def __str__(self):
    return f"{self.food_code} {self.food_name}"

class Mealitem (models.Model):
   meal = models.ForeignKey(Meal, on_delete=models.CASCADE) 
   food_data=models.ForeignKey(Food_Data, on_delete=models.CASCADE)
   mass=models.IntegerField(null=True) 
