from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    title = models.CharField(max_length=100)
    short_url = models.URLField()
    long_url = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    click_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, {self.short_url}"