# Create your models here.

from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(default='Описание')
    keywords = models.CharField(max_length=120, default='Ключевые слова')
    image = models.FileField(null=True, blank=True)
    visible = models.BooleanField(default=1)
    text = models.TextField(default='Текст статьи')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

'''
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/" %(self.id)
 
    class Meta:
        ordering = ["-id", "-timestamp"]
'''