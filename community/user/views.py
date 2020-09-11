from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .forms import LoginForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        passwrod = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and useremail and passwrod and re_password):
            res_data['error'] = '모든 값을 입력해주세요!'
        elif passwrod != re_password:
            res_data['error'] = '비밀번호가 틀립니다!'
        else:
            user = User(
                username=username,
                useremail=useremail,
                password=make_password(passwrod)
            )

            user.save()

        return render(request, 'register.html', res_data)


def page_not_found(request, exception):
    context = {}
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response


def server_error(request):
    context = {}
    response = render(request, "500.html", context=context)
    response.status_code = 500
    return response
