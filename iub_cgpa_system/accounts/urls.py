from django.contrib.auth import views as auth_views
from django.urls import path
from system.views import Home

from . import views

urlpatterns = [
    # path("", views.AuthListView.as_view(template_name="home.html"), name="home"),
    path("", Home.as_view()),
    path(
        "login/",
        views.CustomLoginView.as_view(
            redirect_authenticated_user=True,
            template_name="registration/login.html",
        ),
        name="login",
    ),
    path("profile/<int:pk>", views.ProfileView.as_view(), name="profile"),
    path("accounts/profile/", Home.as_view(), name="profile_view"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    # Change Password
    path(
        "change-password/",
        auth_views.PasswordChangeView.as_view(
            template_name="registration/password_change.html", success_url="change"
        ),
        name="change_password",
    ),
    path(
        "change-password/change/",
        views.PasswordChangedView.as_view(),
        name="change_password_success",
    ),
    # Forget Password
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="password-reset/password_reset.html",
            subject_template_name="password-reset/password_reset_subject.txt",
            email_template_name="password-reset/password_reset_email.html",
            success_url="/login/",
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password-reset/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password-reset/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password-reset/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        "signup/",
        views.SignUpView.as_view(template_name="registration/signup.html"),
        name="signup",
    ),
    path("delete/<int:pk>", views.DeleteProfileView.as_view(), name="delete"),
    path("show/", views.ShowList.as_view(), name="show"),
]
