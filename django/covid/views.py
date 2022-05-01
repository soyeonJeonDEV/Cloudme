from django.shortcuts import render
# Create your views here.
# Create your views here.
from django.http import HttpResponse
from .api import covid_natDeathCnt, covid_natDefCnt, covid_nationNm, covid_nationNmEn
from .api import check_covid,mail

def index(request):    
    natDeathCnt = covid_natDeathCnt
    natDefCnt = covid_natDefCnt
    nationNm = covid_nationNm
    nationNmEn = covid_nationNmEn
    return render(request, 'covid/index.html', {"natDeathCnt": natDeathCnt, "natDefCnt":natDefCnt, "nationNm": nationNm, "nationNmEn": nationNmEn})
