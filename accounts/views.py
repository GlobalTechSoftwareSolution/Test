from django.shortcuts import render, redirect
from .models import UserAccount

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        UserAccount.objects.create(username=username, password=password)
        return redirect("success")
    return render(request, "register.html")

def success(request):
    return render(request, "success.html")
