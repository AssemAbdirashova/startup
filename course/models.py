from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):

    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=5000)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }

