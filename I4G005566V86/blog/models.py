from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User)
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()

