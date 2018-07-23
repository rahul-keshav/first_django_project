from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView

from .models import *


class IndexView(generic.ListView):
    template_name = 'college/index.html'
    context_object_name = 'college'

    def get_queryset(self):
        """Return the last five published questions."""
        return College.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = College
    template_name = 'college/detail.html'

class DepartmentView(generic.DetailView):
    model = Department
    template_name = 'college/department.html'


class CourseView(generic.DetailView):
    model = Course
    template_name = 'college/course.html'

class SemesterView(generic.DetailView):
    model = Semester
    template_name = 'college/year.html'

class SubjectView(generic.DetailView):
    model = Subject
    template_name = 'college/subject.html'

class CollegeCreate(CreateView):
    model = College
    fields = ['name','college_logo','address','city','country']


class DepartmentCreate(CreateView):
    model = Department
    fields = ['College','department_name']



class CourseCreate(CreateView):
    model = Course
    fields = ['department','course_name']

class SemesterCreate(CreateView):
    model = Semester
    fields = ['course','semester_name']






