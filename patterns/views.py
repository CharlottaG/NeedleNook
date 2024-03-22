from django.shortcuts import render
from django.views import generic
from .models import Pattern


# Create your views here.

class PatternList(generic.ListView):
    model = Pattern
    queryset = Pattern.objects.all()
    template_name = "patterns_list.html"
