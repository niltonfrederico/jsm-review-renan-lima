import os
import django
from django.contrib.auth import get_user_model

class SuperuserCreator:
    def __init__(self, username='admin', password='admin', email='admin@example.com'):
        self.username = username
        self.password = password
        self.email = email
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'challenge_juntos.settings')
        django.setup()

        self.User = get_user_model()

    def create_user_admin(self):
        if not self.User.objects.filter(username=self.username).exists():
            self.User.objects.create_superuser(username=self.username, password=self.password, email=self.email)
            print(f"Superuser '{self.username}' created.")
        else:
            print(f"Superuser '{self.username}' already exists.")

def main():
    creator = SuperuserCreator()
    creator.create_user_admin()

if __name__ == "__main__":
    main()
