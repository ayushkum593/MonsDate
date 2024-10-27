from mongoengine import Document, StringField, IntField, ListField
from django.contrib.auth import get_user_model


class UserProfile(Document):
    user = StringField(max_length=50, required=True)
    username = StringField(max_length=50)
    email = StringField()
    age = IntField(null=True, blank=True)
    bio = StringField(max_length=500, blank=True)
    gender = StringField(max_length=10, blank=True)
    location = StringField(max_length=100, blank=True)
    interests = ListField(StringField())  # List of interests as strings

    def __str__(self):
        return self.username
