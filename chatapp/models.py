from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Chat(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.message}'
    
    class Meta:
        ordering = ['-updated_at'] #, '-created_at']


class Room(models.Model):
    name = models.CharField(max_length=90)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
    
