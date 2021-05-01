
from django.contrib.auth.models import User
# from django.apps.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Generate random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix')
        parser.add_argument('-a', '--admin', action='store_true', help='Create an admin account')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs['prefix']
        admin = kwargs['admin']

        for i in range(total):
            if prefix:
                username = '{prefix}_{random_string}'.format(prefix=prefix, random_string=get_random_string())
            else:
                username = get_random_string()

            if admin:
                User.objects.create_superuser(username=username, email='', password='123')
                #self.stdout.write(self.style.SUCCESS('User "%s (%s)" created success!' % (user.username, user_id)))

            else:
                User.objects.create_user(username=username, email='poornima@gmail.com', password='123')
                #self.stdout.write(self.style.SUCCESS('User "%s (%s)" created  success!' % (user.username, user_id)))
