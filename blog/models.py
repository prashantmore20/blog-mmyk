from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    LANGUAGE = [
        ('HI','Hindi'),
        ('MA','Marathi'),
    ]

    TYPE=[
        ('PG', 'Poems & Gazals'),
        ('ST', 'Short Stories'),
    ]
    sNo = models.AutoField(primary_key=True)
    postTitle = models.CharField(max_length=255)
    postSlug = models.CharField(max_length=100,default='NULL')
    postContent = models.TextField()
    postAuthor = models.CharField(max_length=100)
    postLanguage = models.CharField(max_length=2,choices=LANGUAGE,default='MA')
    postType = models.CharField(max_length=2,choices=TYPE,default='PG')
    timeStamp = models.DateTimeField(blank=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return 'Post :' + self.postTitle + ' By: ' + self.postAuthor

class blogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:10] + ".... " + "by " + self.user.first_name
