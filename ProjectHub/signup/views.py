from django.shortcuts import render,redirect

# Create your views here.
def signup(request):
    return render(request,'ProjectHub/signup.html')

