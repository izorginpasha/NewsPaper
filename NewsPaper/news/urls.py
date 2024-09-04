from django.urls import path
# Импортируем созданное нами представление
from .views import (ProductList, ProductDetail, PostList, PostCreate, PostUpdate, PostDelete,
                    upgrade_me, subscribers, CategoryList, unsubscribers, massage)
from django.views.decorators.cache import cache_page

urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым,
    # чуть позже станет ясно почему.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('news/', ProductList.as_view(), name='news_list'),
    path('news/search', cache_page(60*5) (PostList.as_view()), name='news_search'),
    path('news/create',cache_page(60*5) (PostCreate.as_view()), name='news_create'),
    path('news/<int:pk>/edit',cache_page(60*5) (PostUpdate.as_view()), name='news_edit'),
    path('news/<int:pk>/delete',cache_page(60*5) (PostDelete.as_view()), name='news_delete'),
    path('news/upgrade/', upgrade_me, name='upgrade'),
    path('articles/create', PostCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit', PostUpdate.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete', PostDelete.as_view(), name='articles_delete'),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>', ProductDetail.as_view(), name='news_detail'),
    path('',cache_page(60*1) (ProductList.as_view()), name='news_list'),
    path('massage/<int:pk>', massage, name='massage'),

    path('categories/', CategoryList.as_view(), name='categories'),
    path('categories/<int:pk>/subscribers', subscribers, name='subscribers'),
    path('categories/<int:pk>/unsubscribers', unsubscribers, name='unsubscribers'),

]
