from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.
def multi_table(request, number):
    num = number
    result=[]
    index=[]
    for i in range(13):
        result.append(num*i)
    return render(request, 'table.html', {'num':num},{'result':result})
