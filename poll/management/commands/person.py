from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "create a person with name, email, and password"


    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Person\'s name')
        parser.add_argument('email', type=str, help='Person\'s email')
        parser.add_argument('password', type=str, help='Person\'s password')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        email = kwargs['email']
        password = kwargs['password']

        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = name
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created person: {name} ({email})'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating person: {e}'))
   