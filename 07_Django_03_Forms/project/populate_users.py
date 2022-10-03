import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "project.settings"
)  # this configures the settings for the project
# you need to do this before you start manipulating those models

import django

django.setup()

from usersapp.models import User
from faker import Faker


fake = Faker()


def populate(N=10):
    for _ in range(N):
        fake_fullname = fake.name().split()
        fake_email = fake.ascii_safe_email()
        user = User.objects.get_or_create(
            first_name=fake_fullname[0], last_name=fake_fullname[1], email=fake_email
        )[0]


if __name__ == "__main__":
    print("populating users")
    populate()
    print("populating complete")
