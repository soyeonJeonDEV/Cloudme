from django.shortcuts import render
from .api import check_air
# Create your views here.
# Create your views here.
from django.http import HttpResponse

def index(request):
    res = check_air()
    context = {'station': '유럽'}
    return render(request, 'abroad_checker/index.html',context)

def detail(request):
    res = check_air()
    context = {'dust': res}
    return render(request, 'abroad_checker/detail.html', context)