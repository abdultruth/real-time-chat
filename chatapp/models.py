from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=90, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering = ['-updated_at', '-created_at']
    

class Chat(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='chat_room', null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.message}'
    
    class Meta:
        ordering = ['-updated_at','-created_at']



    
