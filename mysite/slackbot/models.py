from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    time_published = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.title


