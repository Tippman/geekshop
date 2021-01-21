from django.core.management import BaseCommand

from authapp.models import User, UserProfile


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            user_profile = UserProfile.objects.create(user=user)