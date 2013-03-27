from django.db import models
from users.models import Users

class Album(models.Model):
    alb_title = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.alb_title

class Picture(models.Model):
    pic_title = models.CharField(max_length=20, blank=True)
    pic = models.ImageField(upload_to='./Pictures/')
    album = models.ForeignKey(Album)

    def __unicode__(self):
        if self.pic_title is None:
            return "New Picture"
        else:
            return self.pic_title

class Sport(models.Model):
    sport_name = models.CharField(max_length=20)
    sport_pic = models.ImageField(upload_to='./Pictures/', default='./Pictures/SportDefault.png')

    def __unicode__(self):
        return self.sport_name

class Article(models.Model):
    date = models.DateTimeField('date published')
    sport_id = models.ForeignKey(Sport)
    gps_file = models.FileField(upload_to='./GpsFiles/', null=True, blank=True)
    art_alb = models.ForeignKey(Album, null=True, blank=True)
    user_id = models.ForeignKey(Users)
    description = models.CharField(max_length=400, blank=True)

    def __unicode__(self):
        return "Articles"

class Post(models.Model):
    art_id = models.ForeignKey(Article)
    user_id = models.ForeignKey(Users)
    content = models.CharField(max_length=400)
    date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.user_id