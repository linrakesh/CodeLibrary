from django.urls import path
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordResetView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetCompleteView
                                       )

from users.views import registeruser, userProfile


urlpatterns = [
    path('register/', registeruser, name="register"),
    path('profile/',  userProfile, name="profile"),
    path('login/', LoginView.as_view(template_name="user/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="user/log_out.html"), name="logout"),
    path('password-reset/', PasswordResetView.as_view(
        template_name="user/password_reset_form.html"), name="password_reset"),

    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name="user/password_reset_done.html"), name="password_reset_done"),


    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name="user/password_reset_confirm.html"), name="password_reset_confirm"),


    path('password-reset-complete/', PasswordResetCompleteView.as_view(
        template_name="user/password_reset_complete.html"), name="password_reset_complete"),

]
