from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=130)
    content = models.TextField()
    datetime = models.DateTimeField()
    def __str__(self):
        return self.title