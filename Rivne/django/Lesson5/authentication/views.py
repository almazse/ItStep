from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages



def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            client_data = form.cleaned_data
            user = authenticate(username=client_data['login'], password=client_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Authenticated successful!")
                    return redirect("/")
                else:
                    return HttpResponse('User blocked!')
            else:
                return HttpResponse('Authenticated blocked!')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect("authentication:login")


def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        city = request.POST['city']
        phone = request.POST['phone']

        user = User.objects.create_user(username=username, email=email, password=password)

        user.first_name = first_name
        user.last_name = last_name

        # user.profile.city = city
        # user.profile.phone = phone

        group = Group.objects.get(name='customers')
        group.user_set.add(user)
        user.save()

        # user = authenticate(username=username, password=password)
        # if user is not None:
        #     if user.is_active:
        #         login(request, user)
        #         messages.success(request, "Authenticated successful!")
        #         return redirect("/")
        #     else:
        #         return HttpResponse('User blocked!')
        # else:
        #     return HttpResponse('Authenticated blocked!')

    return render(request, 'signin.html')
