from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("auth")
    form = NewUserForm
    return render(request, "register.html", context={"form": form, "title": 'Тестовое Табашников'})


def auth(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
        return redirect("main")
    form = AuthenticationForm()
    return render(request, "auth.html", context={"form": form, "title": 'Другая страница'})
