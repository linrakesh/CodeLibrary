from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from users.views import registeruser,userProfile


urlpatterns = [
    path('register/', registeruser, name="register"),
    path('profile/',  userProfile, name="profile"),
    path('login/', LoginView.as_view(template_name = "user/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name = "user/log_out.html"), name="logout"),
]
