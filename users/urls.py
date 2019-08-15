from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from users.views import registeruser


urlpatterns = [
    path('register/', registeruser, name="register"),
    path('login/', LoginView.as_view(template_name = "user/login.html"), name="login"),
    path('logout/', LoginView.as_view(template_name = "user/log_out.html"), name="logout"),
]
