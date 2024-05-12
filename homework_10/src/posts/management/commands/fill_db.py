from django.core.management.base import BaseCommand
from datetime import datetime
from posts.models import Post, Tags, Images
from writers.models import Writer, WriterProfile
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class Command(BaseCommand):
    help = "Fill Db"

    def handle(self, *args, **options):
        def create_writer_with_password(first_name, last_name, email, username, age, password):
            User = get_user_model()
            try:
                # Создаем пользователя
                writer = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, age=age)
                # Устанавливаем хэшированный пароль
                writer.set_password(password)
                # Сохраняем пользователя
                writer.save()
                return writer
            except ValidationError as e:
                print(f"Error: {e}")
                return None
        # Создаем писателей
        u = Writer.objects.filter(username='pushkin').first()
        if not u:
            writer1 = create_writer_with_password('Александр', 'Пушкин', 'pushkin@example.com', 'pushkin', 37, 'P@ssw0rd1')
            writer2 = create_writer_with_password('Лев', 'Толстой', 'tolstoy@example.com', 'tolstoy', 82, 'P@ssw0rd2')
            writer3 = create_writer_with_password('Федор', 'Достоевский', 'dostoevsky@example.com', 'dostoevsky', 59, 'P@ssw0rd3')
            writer4 = create_writer_with_password('Анна', 'Ахматова', 'ahmatova@example.com', 'ahmatova', 76, 'P@ssw0rd4')
            writer5 = create_writer_with_password('Михаил', 'Булгаков', 'bulgakov@example.com', 'bulgakov', 48, 'P@ssw0rd5')
            writer6 = create_writer_with_password('Алексей', 'Толстой', 'atolstoy@example.com', 'atolstoy', 62, 'P@ssw0rd6')
            writer7 = create_writer_with_password('Андрей', 'Платонов', 'aplatonov@example.com', 'aplatonov', 59, 'P@ssw0rd7')
            writer8 = create_writer_with_password('Николай', 'Гоголь', 'gogol@example.com', 'gogol', 42, 'P@ssw0rd8')
            writer9 = create_writer_with_password('Антон', 'Чехов', 'chekhov@example.com', 'chekhov', 44, 'P@ssw0rd9')
            writer10 = create_writer_with_password('Иван', 'Тургенев', 'turgenev@example.com', 'turgenev', 64, 'P@ssw0rd10')
            writer11 = create_writer_with_password('John', 'Doe', 'john@example.com', 'johndoe', 30, 'P@ssw0rd11')
            writer12 = create_writer_with_password('Jane', 'Doe', 'jane@example.com', 'janedoe', 28, 'P@ssw0rd12')
            profile1 = WriterProfile.objects.create(writer=writer1, biography='Александр Пушкин - великий русский поэт.')
            profile2 = WriterProfile.objects.create(writer=writer2, biography='Лев Толстой - классик мировой литературы.')
            profile3 = WriterProfile.objects.create(writer=writer3, biography='Федор Достоевский - русский писатель-философ.')
            profile4 = WriterProfile.objects.create(writer=writer4, biography='Анна Ахматова - выдающаяся русская поэтесса.')
            profile5 = WriterProfile.objects.create(writer=writer5, biography='Михаил Булгаков - автор "Мастера и Маргариты".')
            profile6 = WriterProfile.objects.create(writer=writer6, biography='Алексей Толстой - российский писатель и драматург.')
            profile7 = WriterProfile.objects.create(writer=writer7, biography='Андрей Платонов - мастер русской прозы.')
            profile8 = WriterProfile.objects.create(writer=writer8, biography='Николай Гоголь - русский писатель, создатель реалистической повести.')
            profile9 = WriterProfile.objects.create(writer=writer9, biography='Антон Чехов - классик мировой драматургии.')
            profile10 = WriterProfile.objects.create(writer=writer10, biography='Иван Тургенев - русский писатель и общественный деятель.')
            profile11 = WriterProfile.objects.create(writer=writer11, biography='John Doe is a technology enthusiast.')
            profile12 = WriterProfile.objects.create(writer=writer12, biography='Jane Doe loves traveling and writing about her experiences.')            

        # Создаем теги
        t = Tags.objects.filter(name='Technology').first()
        if not t:
            tag1 = Tags.objects.create(name='Technology')
            tag2 = Tags.objects.create(name='Travel')
            tags_list = ['роман', 'поэма', 'рассказ', 'пьеса', 'повесть', 'эссе', 'стихи', 'драма', 'фантастика', 'детектив']
            for tag_name in tags_list:
                tag = Tags.objects.create(name=tag_name)
                tag.save()

         # Создаем пост

        post1 = Post.objects.create(title='Евгений Онегин', body='Поэма в стихах Александра Пушкина.', published_at=datetime.now(), author=writer1)
        post2 = Post.objects.create(title='Война и мир', body='Роман Льва Толстого о войне 1812 года.', published_at=datetime.now(), author=writer2)
        post3 = Post.objects.create(title='Преступление и наказание', body='Роман Федора Достоевского о преступлении и морали.', published_at=datetime.now(), author=writer3)
        post4 = Post.objects.create(title='Реквием', body='Сборник стихотворений Анны Ахматовой.', published_at=datetime.now(), author=writer4)
        post5 = Post.objects.create(title='Мастер и Маргарита', body='Роман Михаила Булгакова о дьяволе в Москве.', published_at=datetime.now(), author=writer5)
        post6 = Post.objects.create(title='Петр Первый', body='Исторический роман Алексея Толстого о Петре I.', published_at=datetime.now(), author=writer6)
        post7 = Post.objects.create(title='Чевенгур', body='Роман Андрея Платонова о деревенской жизни.', published_at=datetime.now(), author=writer7)
        post8 = Post.objects.create(title='Мертвые души', body='Повесть Николая Гоголя о Российской империи.', published_at=datetime.now(), author=writer8)
        post9 = Post.objects.create(title='Три сестры', body='Пьеса Антона Чехова о жизни трех сестер.', published_at=datetime.now(), author=writer9)
        post10 = Post.objects.create(title='Отцы и дети', body='Роман Ивана Тургенева о столкновении поколений.', published_at=datetime.now(), author=writer10)
        post11 = Post.objects.create(title='First Post', body='This is the body of the first post.', published_at=datetime.now(), author=writer1)
        post12 = Post.objects.create(title='Second Post', body='This is the body of the second post.', published_at=datetime.now(), author=writer2)
    

       # Связываем теги с постами
        post11.tags.add(tag1)
        post11.tags.add(tag2)
        post12.tags.add(tag2)
        post1.tags.add(*Tags.objects.filter(name__in=['поэма', 'стихи']))
        post2.tags.add(*Tags.objects.filter(name='роман'))
        post3.tags.add(*Tags.objects.filter(name='роман'))
        post4.tags.add(*Tags.objects.filter(name='стихи'))
        post5.tags.add(*Tags.objects.filter(name='роман'))
        post6.tags.add(*Tags.objects.filter(name='роман'))
        post7.tags.add(*Tags.objects.filter(name='роман'))
        post8.tags.add(*Tags.objects.filter(name='повесть'))
        post9.tags.add(*Tags.objects.filter(name='пьеса'))
        post10.tags.add(*Tags.objects.filter(name='роман'))

        for i in range(1, 14):
            post = Post.objects.get(id=i)
            image = Images.objects.create(post=post, image_url=f'https://mdbcdn.b-cdn.net/img/new/standard/city/{str(i).zfill(3)}.webp')
            image.save()

        su = Writer.objects.filter(username='vk').first()
        if not su:
            Writer.objects.create_superuser(
                username='vk',
                email='mr_tomat@mail.ru',
                password='pass',
            )

        self.stdout.write(self.style.SUCCESS('DB is ready'))