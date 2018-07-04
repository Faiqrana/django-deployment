from django.shortcuts import render

# Create your views here.

def home(request):


    return render(request,'app_four/home.html')

def other(request):
    dict={'text':'We are other page','number':100}
    return render(request,'app_four/other.html',dict)

