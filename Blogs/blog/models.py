from django.db import models
from django.utils.timezone import now
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

# model number 1 contains the information about the post
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=User.is_active)
    title=models.CharField(max_length=100)
    text=models.TextField(max_length=200)
    create_date=models.DateTimeField(default=now())
    publish_date=models.DateTimeField(null=True,blank=True)

    def approved_comments(self):
        return self.comments.filter(approved=True)

    def publish(self):
        self.publish_date=now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

# model number 2 contains the information about the comments
class Comment(models.Model):
    post=models.ForeignKey('blog.post',related_name='comments',on_delete=models.CASCADE)
    author=models.CharField(max_length=50)
    text=models.TextField(max_length=200)
    created_date=models.DateTimeField(default=now())
    approved=models.BooleanField(default=False)

    def approve(self):
        self.approved=True
        self.save()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("post_list")
