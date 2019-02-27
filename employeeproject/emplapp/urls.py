from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('Employee',views.Employee,name='Employee'),
]