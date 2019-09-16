from django.urls import path
from .views import homeView, singlecode, addCode, updateCode, deleteCode, search_result, tagList, authorView, aboutus, privacy, disclaimer, write_for_us, submit_code, contact_us


urlpatterns = [
    path('', homeView.as_view(), name="home"),
    path('about/', aboutus, name="aboutus"),
    path('privacy/', privacy, name="privacy"),
    path('disclaimer/', disclaimer, name="disclaimer"),
    path('write/', write_for_us, name="write"),
    path('submit/', submit_code, name="submit_code"),
    path('contact/', contact_us, name="contact_us"),
    path('<int:pk>/', singlecode, name="singlecode"),
    path('result/', search_result, name="search_result"),
    path('tag/<slug:tag_slug>/', tagList, name="taglist"),
    path('user/<int:pk>/', authorView, name="authorList"),
    path('add/', addCode.as_view(), name="add"),
    path('<int:pk>/update/', updateCode.as_view(), name="update"),
    path('<int:pk>/delete/', deleteCode.as_view(), name="delete"),

]
