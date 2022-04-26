from django.shortcuts import render

from .api import check_covid,mail


def index(request):
    data = check_covid()
    mail_data = mail()
    num = []
    print(mail_data['tr']['td'])
    for number in mail_data['tr']['td']:
        num.append(number['span'])
    return render(request, 'covid_checker/covid_main.html',{'data':data,'today':num})
        
# Create your views here.
