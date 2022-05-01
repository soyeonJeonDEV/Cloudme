from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Profile 
from django.contrib.auth.models import User
from django.core.cache import cache 
from django.contrib.auth.forms import AuthenticationForm


def index(request):
#    cache.set("testkey", "test_value", timeout=60 * 60)
    return render(request, 'main.html')


def register(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"],
                email=request.POST["email"])
            profile = Profile(
                user=user,
                name=request.POST["name"],
                is_admin=request.POST.get('is_admin', '') == 'on')
            profile.save()
            return redirect('/')
    else:
        return render(request, 'common/register.html')

def login(request):

    if request.method == 'POST':
    	# 첫번째 인자로 request 를 받아야 한다.
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 유효성 검사를 통과하면 세션을 create 해야 함 -> login()
            auth_login(request, form.get_user())
            # url 에 next 가 있을 때랑 없을때 결과가 다름
            return redirect(request.GET.get('next') or 'articles:index')
    else:
    	# 로그인에 필요한 빈 종이를 생성해서 lognin.html 에 전달
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'common/login.html', context)

def change(request):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        profile.name = request.POST["name"]
        profile.is_admin = request.POST.get('is_admin', '') == 'on'
        profile.save()
        return redirect('/')
    else:
        return render(request, 'common/change.html')

#Create your views here.
