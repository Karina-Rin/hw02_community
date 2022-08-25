from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.contrib.auth import get_user_model

User = get_user_model()


def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших зн. к меньшим)
    posts = Post.objects.order_by("-pub_date")[:10]
    # название группы
    title = "Последние обновления на сайте"
    # В словаре context отправляем информацию в шаблон
    context = {
        "posts": posts,
        "title": title,
    }
    return render(request, "posts/index.html", context)


# View-функция для страницы сообщества:
def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.order_by("-pub_date")[:10]
    title = group.__str__
    context = {
        "group": group,
        "posts": posts,
        "title": title,
    }
    return render(request, "posts/group_list.html", context)
