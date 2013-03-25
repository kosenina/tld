from django.db import models

class Album(models.Model):
    alb_title = models.CharField(max_length=20)
    description = models.CharField(max_length=20)

class Picture(models.Model):
    pic_title = models.CharField(max_length=20)
    pic = models.FileField(upload_to='.')
    album = models.ForeignKey(Album)

class User(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    user_pic = models.ForeignKey(Picture)

class Sport(models.Model):
    sport_name = models.CharField(max_length=20)
    sport_pic = models.ForeignKey(Picture)

class GPS(models.Model):
    user_id = models.ForeignKey(User)
    gps_file = models.FileField(upload_to='.')

class Article(models.Model):
    date = models.DateTimeField('date published')
    sport_id = models.ForeignKey(Sport)
    gps_file = models.ForeignKey(GPS)
    art_pic = models.ForeignKey(Picture)

class Post(models.Model):
    art_id = models.ForeignKey(Article)
    user_id = models.ForeignKey(User)
    content = models.CharField(max_length=400)
