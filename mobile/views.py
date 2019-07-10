from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def Home(request):
    #return HttpResponse('<h1>สวัสดีวันอังคาร</h1>')
    return render(request,'mobile/home.html')

def About(request):
    #return HttpResponse('<h1>About Us</h1>')
    return render(request, 'mobile/about.html')

def Product(request):
    #return HttpResponse('<h1>เรือดำน้ำพี่ป้อม</h1>')
    return render(request, 'mobile/product.html')