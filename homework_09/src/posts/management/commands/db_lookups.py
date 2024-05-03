from django.core.management.base import BaseCommand

from posts.models import Post, Tags
from writers.models import Writer, WriterProfile


class Command(BaseCommand):
    help = "Fill Db"

    def handle(self, *args, **options):
        pass
        # animal = Animal.objects.get(id=5)  # -> exc
        # animal = Animal.objects.filter(id=5).first()  # -> None



