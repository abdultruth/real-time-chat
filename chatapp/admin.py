from django.contrib import admin


from .models import Chat, Room

# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'user','room', 'created_at', 'updated_at']
    fields = ['message', 'user', 'room']


class RoomAdmin(admin.ModelAdmin):
    list_display = ['id' ,'name', 'created_at', 'updated_at']
    fields = ['name',]


admin.site.register(Chat, ChatAdmin)
admin.site.register(Room, RoomAdmin)