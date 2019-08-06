from django.urls import path
from .views import home, singlecode

urlpatterns = [
    path('', home, name="home"),
    path('<int:id>/', singlecode, name="singlecode"),

]
