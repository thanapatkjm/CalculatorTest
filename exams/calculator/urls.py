from django.urls import path
from . import views

app_name='cal'
urlpatterns = [
    path('input/',views.input,name='input'),
    path('multi/', views.multi_table, name='multi'),
    path('stat/', views.stat, name='stat'),
    path('order/', views.Number_Order, name='NOrder'),
]
