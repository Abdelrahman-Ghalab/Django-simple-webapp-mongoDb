from mongoengine import *
from django.contrib.auth.models import User
import datetime
connect('myDB')


class Post(Document):
    title = StringField(max_length=120, required=True)
    content = StringField(max_length=500, required=True)
    last_update = DateTimeField(required=True)

class Vacation(Document):
    def __str__(self):
        return "from: " + str(self.start_date)+" to: "+ str(self.end_date)+ " description: "+ self.description  + " total period= " + str(self.total_period)

    #auto_increment_id = models.AutoField(primary_key=True, default=0)
    idd = IntField(default=0)
    employee = StringField(max_length=50, required=True)
    description = StringField(max_length=500)
    start_date = StringField(max_length=10)
    end_date = StringField(max_length=10)
    total_period = IntField(default=0)
