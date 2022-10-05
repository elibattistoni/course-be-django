import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cbv_project.settings') # this configures the settings for the project
# you need to do this before you start manipulating those models

import django
django.setup()

import random
from cbv_app.models import School, Student
from faker import Faker

fakegen = Faker()

def populate(n_schools=5, n_students=10):
    """This function populates the database with fake data

    Args:
        n_schools (int, optional): Number of schools to create. Defaults to 5.
        n_students (int, optional): Number of students per school to create. Defaults to 10.
    """

    for i in range(n_schools):
        fake_name = fakegen.company()
        fake_principal = fakegen.name()
        fake_location = fakegen.address()
        fakeSchool = School.objects.get_or_create(name=fake_name, principal=fake_principal, location=fake_location)[0]

        for j in range(n_students):
            fake_name = fakegen.name()
            fake_age = random.randint(6,18)
            fakeStudent = Student.objects.get_or_create(name=fake_name, age=fake_age, school=fakeSchool)[0]

if __name__ == '__main__':
    print("populating script")
    populate()
    print("populating complete")