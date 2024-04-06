from django.core.management.base import BaseCommand
from datetime import datetime
from posts.models import Post, Tags
from writers.models import Writer, WriterProfile


class Command(BaseCommand):
    help = "Fill Db"

    def handle(self, *args, **options):
        # Создаем писателей
        writer1 = Writer.objects.create(name='John Doe', email='john@example.com', username='johndoe', age=30)
        writer2 = Writer.objects.create(name='Jane Doe', email='jane@example.com', username='janedoe', age=28)

        # Создаем теги
        tag1 = Tags.objects.create(name='Technology')
        tag2 = Tags.objects.create(name='Travel')

        # Создаем посты
        post1 = Post.objects.create(title='First Post', body='This is the body of the first post.', published_at=datetime.now(), author=writer1)
        post2 = Post.objects.create(title='Second Post', body='This is the body of the second post.', published_at=datetime.now(), author=writer2)


        # Связываем теги с постами
        post1.tags.add(tag1)
        post1.tags.add(tag2)
        post2.tags.add(tag2)

        # # Связываем авторов с постами
        # post1.author.add(writer1)
        # post2.author.add(writer2)

        # Создаем профили писателей
        profile1 = WriterProfile.objects.create(writer=writer1, biography='John Doe is a technology enthusiast.')
        profile2 = WriterProfile.objects.create(writer=writer2, biography='Jane Doe loves traveling and writing about her experiences.')

        self.stdout.write(self.style.SUCCESS('DB is ready'))