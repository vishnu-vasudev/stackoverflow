from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=300)
    views = models.IntegerField()
    tags = models.CharField(max_length=100)

class User(models.Model):
    username = models.TextField(max_length=30)
    password = models.CharField(max_length=15)

def __str__(self):
    return self.question
