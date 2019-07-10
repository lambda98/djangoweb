from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, EMS
from .forms import QA
def Home(request):
    #return HttpResponse('<h1>Hello Word</h1>')

    allmobile = Product.objects.all()

    context = {'phonelist': allmobile}
    return render(request, 'mobile/home.html', context)

def About(request):
    return render(request, 'mobile/about.html')

def EMSTracking(request):

    allems = EMS.objects.all()
    contexts = {'emslist': allems}
    return render(request, 'mobile/ems.html', contexts)

def QuestionsForm(request):
    if(request.method == 'POST'):
        form = QA(request.POST)
        if form.is_valid():
           form.save()
           print('Submit Complete')

    form = QA()
    return render(request,'mobile/form.html',{'forms':form})

# def Product(request):
#     return HttpResponse('<h1>Product To Sale</h1>')


