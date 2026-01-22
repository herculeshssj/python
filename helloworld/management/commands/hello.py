from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help = 'Hello World Command :)'

    def handle(self, *args, **options):
        print("Hello World :)")
