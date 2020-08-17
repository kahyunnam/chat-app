from django.contrib import admin

from .models import Chatroom, Message, Comment
admin.site.register(Chatroom)
admin.site.register(Message)
admin.site.register(Comment)
