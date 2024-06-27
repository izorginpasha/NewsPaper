from django.urls import path
# Импортируем созданное нами представление
from .views import (ProductList, ProductDetail, PostList, PostCreate, PostUpdate, PostDelete,
                    ArticlesCreate, ArticlesUpdate, ArticlesDelete)

urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым,
    # чуть позже станет ясно почему.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', ProductList.as_view(), name='news_list'),
    path('search', PostList.as_view(), name='news_search'),
    path('news/create', PostCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit', PostUpdate.as_view(), name='news_edit'),
    path('news/<int:pk>/delete', PostDelete.as_view(), name='news_delete'),
    path('articles/create', ArticlesCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit', ArticlesUpdate.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete', ArticlesDelete.as_view(), name='articles_delete'),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>', ProductDetail.as_view(), name='news_detail'),
]
