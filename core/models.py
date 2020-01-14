from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Message(models.Model):
    body = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Message de: {self.user} : {self.body}'
