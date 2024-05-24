from django.urls import path, reverse_lazy
from . import views as v
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("login/", v.user_login, name="login"),
    path("logout/", v.UserLogoutView.as_view(
        http_method_names=["get", "post", "options"]),
         name="logout"),
    path("", v.home, name="home"),
    path("change_password/", auth_view.PasswordChangeView.as_view(
        template_name="users/password_change.html",
        success_url=reverse_lazy('login')),
        name="change_password"),
    path('password_reset/', auth_view.PasswordResetView.as_view(
        template_name="users/password_reset.html"),
         name='password_reset'),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(
             template_name="registration/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_view.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path("register/", v.register, name='register'),
    path("edit/", v.edit, name='edit'),

]
