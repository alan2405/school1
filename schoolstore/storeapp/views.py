from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
    return HttpResponse("HELLO")

def home(request):
    return render(request,"base.html")

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def content(request):
    return render(request,'content.html')

def form(request):
    return render(request,'form.html')