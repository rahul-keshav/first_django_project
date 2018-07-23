from django.db import models
from django.utils.timezone import now
from django.urls import reverse

# Create your models here.


class College(models.Model):
    name = models.CharField(max_length=50)
    college_logo=models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=now)
    address=models.CharField(max_length=100)
    city= models.CharField(max_length=50)
    country=models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('college:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name +'-' +self.address +'-'+ self.city


class Department(models.Model):
    College = models.ForeignKey(College, on_delete=models.CASCADE,)
    department_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=now)

    def get_absolute_url(self):
        return reverse('college:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.department_name

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE,)
    course_name=models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=now)

    def get_absolute_url(self):
        return reverse('college:department', kwargs={'pk': self.pk})

    def __str__(self):
        return self.course_name


class Semester(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=now)

    def get_absolute_url(self):
        return reverse('college:course', kwargs={'pk': self.pk})

    def __str__(self):
        return self.semester_name


class Subject(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=now)

    def get_absolute_url(self):
        return reverse('college:semester', kwargs={'pk': self.pk})

    def __str__(self):
        return self.subject_name


class Type(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    type = models.CharField(max_length=51)
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=now)
    note=models.FileField()





