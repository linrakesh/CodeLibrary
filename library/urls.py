from django.urls import path
from .views import homeView, singlecode, addCode, updateCode, deleteCode, search_result, tagList, authorView


urlpatterns = [
    path('', homeView.as_view(), name="home"),
    path('<int:pk>/', singlecode, name="singlecode"),
    path('result/', search_result, name="search_result"),
    path('tag/<slug:tag_slug>/', tagList, name="taglist"),
    path('user/<int:pk>/', authorView, name="authorList"),
    path('add/', addCode.as_view(), name="add"),
    path('<int:pk>/update/', updateCode.as_view(), name="update"),
    path('<int:pk>/delete/', deleteCode.as_view(), name="delete"),

]
