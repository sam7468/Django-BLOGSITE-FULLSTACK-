from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #user will be a seperate table
from django.urls import reverse

class Post(models.Model):
     author = models.ForeignKey(User, on_delete=models.CASCADE) #one to many relationship
     title = models.CharField(max_length=100)
     content = models.TextField()
     date_posted = models.DateTimeField(default=timezone.now)


     def __str__(self):
      return self.title

     def get_absolute_url(self):
          return reverse('post-detail',kwargs={'pk':self.pk})