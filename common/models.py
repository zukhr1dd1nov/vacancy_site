from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_employer = models.BooleanField(default=False)

class Employer(models.Model):
    company_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=9)
    hirer = models.OneToOneField(User, on_delete=models.RESTRICT, related_name='extra', related_query_name='extra')

    def __str__(self):
        return self.company_name

class MessageModel(models.Model):
    reason = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)