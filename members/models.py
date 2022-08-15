from django.db import models

class Members(models.Model):
  Username = models.CharField(max_length=255)
  Password = models.CharField(max_length=255)
  Email    = models.CharField(max_length=255,null=True)

class Lost(models.Model):
  Name = models.CharField(max_length=255)
  photo = models.ImageField(upload_to = "Lost_Images")
  date = models.DateTimeField(auto_now_add = True)

class Find(models.Model):
  photo = models.ImageField(upload_to = "Find_Images")
  date = models.DateTimeField(auto_now_add = True)