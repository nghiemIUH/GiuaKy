from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, get_user_model, authenticate
# Create your views here.

User = get_user_model()


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        data = request.POST
        username = data['uname']
        password = data['psw']
        user = authenticate(
            username=username, password=password)
        login(request, user)
        return redirect('/')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        data = request.POST
        file = request.FILES['avatar']

        username = data['uname']
        password = data['psw']
        email = data['email']
        user = User.objects.create_user(
            username=username, password=password, email=email, avatar=file)
        user.save()
        return redirect('/user/login')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/user/login/')
