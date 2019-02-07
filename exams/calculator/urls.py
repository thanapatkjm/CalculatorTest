from django.urls import path
from . import views

app_name='cal'
urlpatterns = [
    path('input/',views.input,name='input'),
    path('', views.multi_table, name='multi'),
]
