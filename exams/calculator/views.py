from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.
def multi_table(request, number):
    num = number
    return render(request, 'table.html', {'number':number})
