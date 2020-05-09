import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

#FAke pop JavaScript
import random
from first_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()

topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choices(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new web[age entry

        webpg = Webpage.objects.get_or_create(topic = top, url=fake_url,name = fake_name)[0]

        #create the fake access AccessRecord
        accrec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__=='__main__':
    print("populating")
    populate(20)
    print("populating complete")
