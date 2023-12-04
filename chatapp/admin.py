from django.contrib import admin


from .models import Chat, Room

# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_display = ['message', 'user', 'created_at', 'updated_at']
    fields = ['message', 'user']


class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    fields = ['name','chat']


admin.site.register(Chat, ChatAdmin)
admin.site.register(Room, RoomAdmin)