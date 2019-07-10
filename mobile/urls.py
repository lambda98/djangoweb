from django.urls import path
from .views import Home,About,EMSTracking,QuestionsForm
urlpatterns = [
    path('', Home, name='mobile-home'),
    path('about/', About, name='mobile-about'),
    path('ems/', EMSTracking, name='mobile-ems'),
    path('questions/', QuestionsForm, name='mobile-qa'),
    #path('product/', Product, name='mobile-product')
]
