from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    # Главная страница
    path("", views.index, name="index"),
    # Страница групп
    path("posts/", views.group_posts, name="posts"),
    # Подробная информация о постах. Ждем пременную типа slug
    path("group/<slug:slug>/", views.group_posts, name="group_list"),
]
