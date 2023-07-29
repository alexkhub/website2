from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):

    return render(request, 'additional_admin_features/main_page.html')
