from django.urls import path
from .views import homeView, singlecode, search_result

urlpatterns = [
    path('', homeView.as_view(), name="home"),
    path('<int:id>/', singlecode, name="singlecode"),
    path('result/', search_result, name="search_result"),


]
