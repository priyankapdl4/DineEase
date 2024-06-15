from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
   
   return render(request, "index.html")

def aboutUsPage(request):
   
   return render(request, "aboutus.html")





