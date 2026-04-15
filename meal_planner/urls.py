"""
URL configuration for meal_planner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from food_adder.views import my_hello
from food_adder.views import start_meal
from food_adder.views import my_view_name
from food_adder.views import meal_list
from food_adder.views import meal_update
from food_adder.views import meal_delete

# from food_adder.templates import food_add
#from meal_planner.views import my_hello
urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('hello/<int:id>', my_hello, name='my_view'),
    path('edit_meal/', my_hello, name='start2'),
    #path('hello2/', my_view_name, name='my_view'),
    path('start_meal/', start_meal, name='start'),
    # path('food_add', food_add, name="food adder")
    path('meal_list/',meal_list, name="meal_list"),
    path('meal_update/<int:id>',meal_update, name="meal_update"),
    path('meal_delete/<int:id>',meal_delete, name="meal_delete")
]
