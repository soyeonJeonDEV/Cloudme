from django.shortcuts import render

from .api import check_covid


def index(request):
    date, data = check_covid()
    return render(request, 'covid_checker/covid_main.html',
        {'date': date, 
          #  'domestic': data[0], 
        # 'abroad': data[1],
        # 'confirm': data[2], 'release': data[3], 'isolation': data[4],
        # 'death': data[5]})
        })
# Create your views here.
