from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "gulatikalash05@gmail.com", "1234")
            print("✅ Superuser Created: admin | 1234")
        else:
            print("Admin already exists")
