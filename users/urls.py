from django.urls import path
from users.views import registeruser


urlpatterns = [
    path('', registeruser, name="register-user"),
]
