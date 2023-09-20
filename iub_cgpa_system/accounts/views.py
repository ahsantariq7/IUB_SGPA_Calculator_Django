from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import SignUpForm
from .models import my_store


class OnlyProfileView(TemplateView):
    template_name = "registration/profile.html"


class CustomLoginView(auth_views.LoginView):
    template_name = ("registration/login.html",)


class ProfileView(UpdateView):
    model = User
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
    ]
    template_name = "registration/profile.html"
    success_url = reverse_lazy("home")


class PasswordChangedView(TemplateView):
    template_name = "registration/success_password_change.html"


# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")


class AuthListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "home.html"
    context_object_name = "ahsan"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myname"] = "My name is"
        return context


class DeleteProfileView(DeleteView):
    model = User
    template_name = "registration/delete.html"
    success_url = reverse_lazy("home")


class ShowList(LoginRequiredMixin, ListView):
    model = my_store
    template_name = "home.html"
    context_object_name = "ahsan"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ahs"] = "Helo"
        return context
