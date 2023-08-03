from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'working_with_orders/basket.html')
