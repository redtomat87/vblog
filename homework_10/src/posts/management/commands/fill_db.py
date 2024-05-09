from django.core.management.base import BaseCommand
from datetime import datetime
from posts.models import Post, Tags, Images
from writers.models import Writer, WriterProfile
from myauth.models import VblogUser


class Command(BaseCommand):
    help = "Fill Db"

    def handle(self, *args, **options):
        # # Создаем писателей
        # writer1 = Writer.objects.create(name='Александр Пушкин', email='pushkin@example.com', username='pushkin', age=37)
        # writer2 = Writer.objects.create(name='Лев Толстой', email='tolstoy@example.com', username='tolstoy', age=82)
        # writer3 = Writer.objects.create(name='Федор Достоевский', email='dostoevsky@example.com', username='dostoevsky', age=59)
        # writer4 = Writer.objects.create(name='Анна Ахматова', email='ahmatova@example.com', username='ahmatova', age=76)
        # writer5 = Writer.objects.create(name='Михаил Булгаков', email='bulgakov@example.com', username='bulgakov', age=48)
        # writer6 = Writer.objects.create(name='Алексей Толстой', email='atolstoy@example.com', username='atolstoy', age=62)
        # writer7 = Writer.objects.create(name='Андрей Платонов', email='aplatonov@example.com', username='aplatonov', age=59)
        # writer8 = Writer.objects.create(name='Николай Гоголь', email='gogol@example.com', username='gogol', age=42)
        # writer9 = Writer.objects.create(name='Антон Чехов', email='chekhov@example.com', username='chekhov', age=44)
        # writer10 = Writer.objects.create(name='Иван Тургенев', email='turgenev@example.com', username='turgenev', age=64)
        # writer11 = Writer.objects.create(name='John Doe', email='john@example.com', username='johndoe', age=30)
        # writer12 = Writer.objects.create(name='Jane Doe', email='jane@example.com', username='janedoe', age=28)

        # # Создаем теги
        # tag1 = Tags.objects.create(name='Technology')
        # tag2 = Tags.objects.create(name='Travel')
        # tags_list = ['роман', 'поэма', 'рассказ', 'пьеса', 'повесть', 'эссе', 'стихи', 'драма', 'фантастика', 'детектив']
        # for tag_name in tags_list:
        #     tag = Tags.objects.create(name=tag_name)
        #     tag.save()

        #  # Создаем посты
        # post1 = Post.objects.create(title='Евгений Онегин', body='Поэма в стихах Александра Пушкина.', published_at=datetime.now(), author=writer1)
        # post2 = Post.objects.create(title='Война и мир', body='Роман Льва Толстого о войне 1812 года.', published_at=datetime.now(), author=writer2)
        # post3 = Post.objects.create(title='Преступление и наказание', body='Роман Федора Достоевского о преступлении и морали.', published_at=datetime.now(), author=writer3)
        # post4 = Post.objects.create(title='Реквием', body='Сборник стихотворений Анны Ахматовой.', published_at=datetime.now(), author=writer4)
        # post5 = Post.objects.create(title='Мастер и Маргарита', body='Роман Михаила Булгакова о дьяволе в Москве.', published_at=datetime.now(), author=writer5)
        # post6 = Post.objects.create(title='Петр Первый', body='Исторический роман Алексея Толстого о Петре I.', published_at=datetime.now(), author=writer6)
        # post7 = Post.objects.create(title='Чевенгур', body='Роман Андрея Платонова о деревенской жизни.', published_at=datetime.now(), author=writer7)
        # post8 = Post.objects.create(title='Мертвые души', body='Повесть Николая Гоголя о Российской империи.', published_at=datetime.now(), author=writer8)
        # post9 = Post.objects.create(title='Три сестры', body='Пьеса Антона Чехова о жизни трех сестер.', published_at=datetime.now(), author=writer9)
        # post10 = Post.objects.create(title='Отцы и дети', body='Роман Ивана Тургенева о столкновении поколений.', published_at=datetime.now(), author=writer10)
        # post11 = Post.objects.create(title='First Post', body='This is the body of the first post.', published_at=datetime.now(), author=writer1)
        # post12 = Post.objects.create(title='Second Post', body='This is the body of the second post.', published_at=datetime.now(), author=writer2)


        # # Связываем теги с постами
        # post11.tags.add(tag1)
        # post11.tags.add(tag2)
        # post12.tags.add(tag2)
        # post1.tags.add(*Tags.objects.filter(name__in=['поэма', 'стихи']))
        # post2.tags.add(*Tags.objects.filter(name='роман'))
        # post3.tags.add(*Tags.objects.filter(name='роман'))
        # post4.tags.add(*Tags.objects.filter(name='стихи'))
        # post5.tags.add(*Tags.objects.filter(name='роман'))
        # post6.tags.add(*Tags.objects.filter(name='роман'))
        # post7.tags.add(*Tags.objects.filter(name='роман'))
        # post8.tags.add(*Tags.objects.filter(name='повесть'))
        # post9.tags.add(*Tags.objects.filter(name='пьеса'))
        # post10.tags.add(*Tags.objects.filter(name='роман'))

        # # # Связываем авторов с постами
        # # post1.author.add(writer1)
        # # post2.author.add(writer2)

        # # Создаем профили писателей

        # profile1 = WriterProfile.objects.create(writer=writer1, biography='Александр Пушкин - великий русский поэт.')
        # profile2 = WriterProfile.objects.create(writer=writer2, biography='Лев Толстой - классик мировой литературы.')
        # profile3 = WriterProfile.objects.create(writer=writer3, biography='Федор Достоевский - русский писатель-философ.')
        # profile4 = WriterProfile.objects.create(writer=writer4, biography='Анна Ахматова - выдающаяся русская поэтесса.')
        # profile5 = WriterProfile.objects.create(writer=writer5, biography='Михаил Булгаков - автор "Мастера и Маргариты".')
        # profile6 = WriterProfile.objects.create(writer=writer6, biography='Алексей Толстой - российский писатель и драматург.')
        # profile7 = WriterProfile.objects.create(writer=writer7, biography='Андрей Платонов - мастер русской прозы.')
        # profile8 = WriterProfile.objects.create(writer=writer8, biography='Николай Гоголь - русский писатель, создатель реалистической повести.')
        # profile9 = WriterProfile.objects.create(writer=writer9, biography='Антон Чехов - классик мировой драматургии.')
        # profile10 = WriterProfile.objects.create(writer=writer10, biography='Иван Тургенев - русский писатель и общественный деятель.')
        # profile11 = WriterProfile.objects.create(writer=writer11, biography='John Doe is a technology enthusiast.')
        # profile12 = WriterProfile.objects.create(writer=writer12, biography='Jane Doe loves traveling and writing about her experiences.')


        for i in range(1, 14):
            post = Post.objects.get(id=i)
            image = Images.objects.create(post=post, image_url=f'https://mdbcdn.b-cdn.net/img/new/standard/city/{str(i).zfill(3)}.webp')
            image.save()

        su = VblogUser.objects.filter(username='vk').first()
        if not su:
            VblogUser.objects.create_superuser(
                username='vk',
                email='mr_tomat@mail.ru',
                password='pass',
            )

        self.stdout.write(self.style.SUCCESS('DB is ready'))