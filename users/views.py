from django.shortcuts import render, redirect, reverse, reverse_lazy
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from . import forms

# Create your views here.


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


# def post(self, request):
#     form = forms.LoginForm(request.POST)
#     if form.is_valid():
#         email = form.cleaned_data.get("email")
#         password = form.cleaned_data.get("password")
#         user = authenticate(request, username="email", password="password")
#     return render(request, "users/login.html", {"form": form})
