from django.shortcuts import render

from .api import check_covid


def index(request):
    data = check_covid()
    return render(request, 'covid_checker/covid_main.html',data)
        
# Create your views here.
