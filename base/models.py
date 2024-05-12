from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):

    topic_name = models.CharField(max_length=50)


class Author(models.Model):

    name = models.CharField(max_length=50)


class Novel(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', null = False, on_delete=models.CASCADE)
    # author = models.CharField(max_length=50)
    topic = models.ForeignKey('Topic', null = True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    veiws = models.IntegerField(null=False)




class Comment(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    content = models.CharField(max_length=2000)