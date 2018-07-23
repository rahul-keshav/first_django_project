from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import *


class IndexView(generic.ListView):
    template_name = 'school/index.html'
    context_object_name = 'school'

    def get_queryset(self):
        """Return the last five published questions."""
        return School.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = School
    template_name = 'school/detail.html'


class ClassView(generic.DetailView):
    model = Class
    template_name = 'school/class.html'


class SubjectView(generic.DetailView):
    model = Subject
    template_name = 'school/subject.html'


class SchoolCreate(CreateView):
    model = School
    fields = ['name','school_logo','address','city','country']
