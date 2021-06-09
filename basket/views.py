from django.shortcuts import render
from django.http import HttpResponse


def basket_summary(request):
    return render(request, 'basket/summary.html')
