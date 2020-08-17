from django.db import models
from django.contrib.auth.models import User

class Chatroom(models.Model):
	text = models.CharField(max_length = 1000)
	date_added = models.DateTimeField(auto_now_add = True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__ (self):
	#return model but string
		return self.text


class Message(models.Model):
	chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'messages'
 
	def __str__ (self):
		return f"{self.text[:100]}..."


class Comment(models.Model):
	message = models.ForeignKey(Message, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'comments'

	def __str__ (self):
		return f"{self.text[:50]}..."