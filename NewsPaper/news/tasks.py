from celery import shared_task
from .models import Category, Author, Post, PostCategory, Comment, User
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

import time
@shared_task
def send_email_createPost(user, news):
    b = PostCategory.objects.filter(post=news.id).values('category')
    i = b[0]
    category = i.get('category')
    users = Category.objects.get(pk=category).subscribers.all()

    for user in users:
        if user.email:
            send_mail(

                subject=news.title_news[:124] + "...",
                # имя клиента и дата записи будут в теме для удобства
                message=f'Здравствуй, {user}. Новая статья в твоём любимом разделе!    '
                        f'Краткое содержание:{news.text_news}...  '  # сообщение с кратким описанием проблемы
                        f'Портобнo  http://127.0.0.1:8000/{news.id}',
                from_email='izorgin.pasha@yandex.ru',
                # здесь указываете почту, с которой будете отправлять (об этом попозже)
                recipient_list=[user.email]  # здесь список получателей. Например, секретарь, сам врач и т. д.
            )
        else:
            print("not email")
@shared_task
def weekly_newsletter():
    now = datetime.now()
    days_to_subtract = 7
    new_date = now - timedelta(days=days_to_subtract)
    post_list = Post.objects.filter(time_in=new_date).all()
    users = User.objects.all()

    for user in users:
        if user.email:
            send_mail(

                subject='send',
                # имя клиента и дата записи будут в теме для удобства
                message=f'Здравствуй, {user}. Новая статьи!    '
                        f'Краткое содержание:{post_list.text_news[:124] + "..."}'# сообщение с кратким описанием проблемы
                        f'Портобнo  http://127.0.0.1:8000/{post_list.id}',
                from_email='izorgin.pasha@yandex.ru',
                # здесь указываете почту, с которой будете отправлять (об этом попозже)
                recipient_list=[user.email]  # здесь список получателей. Например, секретарь, сам врач и т. д.
            )
        else:
            print("not email")