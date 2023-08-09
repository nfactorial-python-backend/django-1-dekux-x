from django.urls import path

from . import views

urlpatterns = [
    path("", views.greet, name="greet"),
    path("<int:first>/add/<int:second>/", views.add, name="add" ),
    path("transform/<str:text>/", views.upper, name="upper"),
    path("check/<str:word>/", views.polindrome, name= "polindrome"),
    path("calc/<int:first>/<str:operation>/<int:second>/", views.calculator, name="calculator")
]