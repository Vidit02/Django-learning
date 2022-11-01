from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    print(request)
    return HttpResponse("Hello World")

def aboutUs(request):
    return render(request,'aboutus.html')

def contactUs(request):
    data = {
        "firstName" : "Vidit",
        "lastName" : "Gandhi"
    }
    return render(request,'contactus.html',data )