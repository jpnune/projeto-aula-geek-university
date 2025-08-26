from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username=os.environ.get('DJANGO_SUPERUSER_USERNAME')).exists():
            User.objects.create_superuser(
                username=os.environ.get('DJANGO_SUPERUSER_USERNAME'),
                password=os.environ.get('DJANGO_SUPERUSER_PASSWORD'),
                email=os.environ.get('DJANGO_SUPERUSER_EMAIL'),
            )