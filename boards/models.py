from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

class Board(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    board = models.ForeignKey(Board,related_name='topics',on_delete=models.CASCADE)
    crated_by = models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.board.name+self.subject
    

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic,related_name='posts',on_delete=models.CASCADE)
    crated_by = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = RichTextField()

class Author(models.Model):
    name = models.CharField(max_length=50)
    phone = PhoneNumberField(blank=True)
    
    def __str__(self) -> str:
        return self.name
    
