from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'table/table.html')