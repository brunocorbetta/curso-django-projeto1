from django.urls import path

from . import views  # o . e da pasta onde estou

urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('recipes/<int:id>/', views.recipe, name="recipes-recipe"),

]
