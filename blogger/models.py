from django.db import models
from django.utils.timezone import now


# Create your models here.

class Profile(models.Model):
    first_name=models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

    email_id= models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    pub_date = models.DateTimeField(default=now)



class Stacks(models.Model):
    name=models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=now)


class Blog(models.Model):
    name=models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=now)


class Liked_notes(models.Model):
    name = models.CharField(max_length=15)



class Liked_institutes(models.Model):
    name = models.CharField(max_length=15)


class Liked_bloggers(models.Model):
    name = models.CharField(max_length=15)


