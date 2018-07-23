from django.db import models
from django.utils.timezone import now
from django.urls import reverse


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=50)
    school_logo= models.CharField(max_length=500)
    pub_date = models.DateTimeField(default=now)
    address=models.CharField(max_length=100)
    city= models.CharField(max_length=50)
    country=models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('school:detail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.name +'-' +self.address +'-'+ self.city


class Board(models.Model):
    board_name=models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=now)


class Class(models.Model):
    course = models.ForeignKey(Board, on_delete=models.CASCADE)
    class_name=models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=now)



class Subject(models.Model):
    department = models.ForeignKey(Class, on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=now)


class Type(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=now)
    note = models.FileField()
