from django.shortcuts import render


# Create your views here.
def first_app(request):
    return render(request,'first_app.html')
def first_app1(request):
    return render(request,'first_app1.html')
