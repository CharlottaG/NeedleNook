from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class AddPattern(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = slug = models.SlugField(max_length=200, unique=True)
    created_by= models.ForeignKey(User, on_delete=models.CASCADE, related_name="knitting_pattern")
    instructions = models.TextField()
    needles = models.CharField(max_length=20)
    yarn = models.CharField(max_length=20)
    gauge = models.CharField(max_length=20)
    difficulty_level = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on= models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    