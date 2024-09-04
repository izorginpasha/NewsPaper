from django.core.management.base import BaseCommand, CommandError
from news.models import Category, Author, Post, PostCategory, Comment, User

# /доделать
class Command(BaseCommand):
    help = 'Удаление новостей из категории'
    missing_args_message = 'Недостаточно аргументов'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return
        try:
            category = Category.objects.get(category=options['category'])
            postCategory = PostCategory.objects.get(category_id=category.id)
            self.stdout.write(self.style.SUCCESS(
                f'Succesfully deleted all news from category {category.category}'))  # в случае неправильного подтверждения говорим, что в доступе отказано
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category '))
