from django.urls import path
from . import views

app_name='cal'
urlpatterns = [
    path('<int:number>', views.multi_table, name='multi'),
]
