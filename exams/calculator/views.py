from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.
def multi_table(request, number):
    num = number
    result=[]
    for i in range(13):
        reserv = ""+str(num)+" x "+str(i)+" = "+str(num*i)+"    : "
        result.append(reserv)
    return HttpResponse(result)
