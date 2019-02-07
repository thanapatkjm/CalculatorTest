from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Create your views here.
def input(request):
    return render(request,'input.html')

def multi_table(request):
    num = request.POST['input']
    result=[]
    for i in range(13):
        reserv = ""+str(num)+" x "+str(i)+" = "+str(num*i)+"    : "
        result.append(reserv)
    return render(request, 'table.html',{'num':num},{'result':result})
