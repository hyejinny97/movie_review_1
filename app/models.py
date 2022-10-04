from email.policy import default
from django.db import models
from django.forms import ModelChoiceField

# Create your models here.

class Review (models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    star_point = models.IntegerField(default=0)
    