import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project_one.settings') # this configures the settings for the project
# you need to do this before you start manipulating those models

import django
django.setup()

import random
from app_one.models import Topic,Webpage,AccessRecord
from faker import Faker


fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0] # return the first element of the tuple
    t.save()
    return t

def populate(N=5):
    
    for entry in range(N):

        # get the topic for the entry
        top = add_topic()

        # create fake data for that entry
        fake_url = fakegen.url() # get a fake url
        fake_date = fakegen.date()
        fake_name = fakegen.company() # get a fake company name for this website

        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        #! if in a model, one field is a foreign key, you have to pass an instance of that foreign key object
        #! not a string

        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("populating complete")