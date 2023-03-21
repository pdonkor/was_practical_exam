from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    date = models.DateField()
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

#news title, author, date, and the description text