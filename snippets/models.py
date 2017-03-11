from django.db import models

# Create your models here.
class Snippet(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    language = models.CharField(max_length=256, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    description = models.TextField(max_length=256, blank=False, null=False)

    def __str__(self):
        """ Returns a human readable version of the snippet object """
        return '\nTitle: %s\n Language: %s\n Text: %s\n Description: %s\n' % (self.title, self.language, self.text, self.description)