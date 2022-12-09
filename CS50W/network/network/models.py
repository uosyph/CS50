from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    content = models.CharField(max_length=280)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'POST "{self.id}" BY "{self.user}" ON "{self.date.strftime("%d %b %Y %H:%M:%S")}"'
