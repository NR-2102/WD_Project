from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import Profile

class Command(BaseCommand):
    help = 'Creates profiles for all existing users'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        created_count = 0
        existing_count = 0

        for user in users:
            try:
                # Try to get existing profile
                profile = user.profile
                existing_count += 1
            except Profile.DoesNotExist:
                # Create new profile if it doesn't exist
                Profile.objects.create(user=user)
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully processed {users.count()} users:\n'
                f'- Created {created_count} new profiles\n'
                f'- Found {existing_count} existing profiles'
            )
        ) 