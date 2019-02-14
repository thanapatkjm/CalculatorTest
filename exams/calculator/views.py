from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Number_times


def input(request):
    return render(request,'input.html')

def Number_Order(request):
    data = Number_times.objects.values().all().order_by('number')
    fields_name = Number_times._meta.fields
    return render(request,'stat.html',{'data':data,'fields_name':fields_name})

def stat(request):
    fields_name = Number_times._meta.fields
    data = Number_times.objects.values().all()
    return render(request,'stat.html',{'data':data,'fields_name':fields_name})

def multi_table(request):
    num = request.POST['input']
    try:
        numbers = Number_times.objects.get(number=num)
        numbers.times = numbers.times+1
    except:
        numbers = Number_times(number=num,times=0)
        numbers.times = numbers.times+1
    times = numbers.times
    numbers.save()
    result=[]
    for i in range(13):
        re = int(num)*i
        reserv = ""+str(num)+" x "+str(i)+" = "+str(re)+"    : "
        result.append(reserv)
    return render(request, 'table.html',{'num':num, 'result':result,'times':times})
