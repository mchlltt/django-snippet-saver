from django.db import models

# Create your models here.
class Snippet(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    language = models.CharField(max_length=256, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    description = models.TextField(max_length=256, blank=False, null=False)