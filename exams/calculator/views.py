from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Number_times


def input(request):
    return render(request,'input.html')

def multi_table(request):
    num = request.POST['input']
    numbers = Number_times(number=num)

    try:
        numbers = Number_times.objects.get(number=num)
    except:
        numbers = Number_times(number=num)
        numbers.times = number.times+1
    result=[]

    for i in range(13):
        reserv = ""+str(num)+" x "+str(i)+" = "+str(num*i)+"    : "
        result.append(reserv)
    return render(request, 'table.html',{'num':num, 'result':result,'numbers':numbers})
