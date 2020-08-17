"""Defines URL patterns for chat_app"""

from django.urls import path

from . import views

app_name = 'chat_app'
urlpatterns = [
	#Home page
	path('',views.index, name = 'index'),
	#Page that shows all chatrooms
	path('chatrooms/', views.chatrooms, name = 'chatrooms'),
	#Chatroom description page
	path('chatrooms/<int:chatroom_id>/', views.chatroom, name='chatroom'),
	#Make new Chatroom
	path('new_chatroom/', views.new_chatroom, name = 'new_chatroom'),
	#Write a message in a chatroom
	path('new_message/<int:chatroom_id>/', views.new_message, name = 'new_message'),
	#Editing an entry
	path('edit_message/<int:message_id>/', views.edit_message, name = 'edit_message'),
]