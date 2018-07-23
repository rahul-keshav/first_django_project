from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import *


class IndexView(generic.ListView):
    template_name = 'blogger/index.html'
    context_object_name = 'blog'

    def get_queryset(self):
        """Return the last five published questions."""
        return Blog.objects.order_by('-pub_date')[:5]

