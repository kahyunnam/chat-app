from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

from .models import Chatroom, Message
from .forms import ChatroomForm, MessageForm

def index(request):
	"""show home page"""
	return render(request, 'chat_app/index.html')

def chatrooms(request):
	"""show chatrooms"""
	chatrooms = Chatroom.objects.order_by('date_added')
	context = {'chatrooms':chatrooms}
	return render(request, 'chat_app/chatrooms.html',context)

def chatroom(request, chatroom_id):
	"""show individual chatroom and messages"""
	chatroom = Chatroom.objects.get(id=chatroom_id)
	messages = chatroom.message_set.order_by('-date_added')
	context = {'chatroom':chatroom, 'messages':messages}
	return render(request, 'chat_app/chatroom.html', context)

@login_required
def new_chatroom(request):
	"""Add a new topic."""
	if request.method != 'POST':
		# nothing = blank
		form = ChatroomForm()

	else:
		# something
		form = ChatroomForm(data=request.POST)
		if form.is_valid():
			new_chatroom = form.save(commit=False)
			new_chatroom.owner = request.user
			new_chatroom.save()
			return redirect('chat_app:chatrooms')

	context = {'form':form}
	return render(request, 'chat_app/new_chatroom.html', context)

@login_required
def new_message(request, chatroom_id):
	"""write a message in a chatroom"""
	chatroom = Chatroom.objects.get(id = chatroom_id)

	if request.method != 'POST':
		#nothing = blank
		form = MessageForm()
	else:
		# POST data submitted; process data
		form = MessageForm(data=request.POST)
		if form.is_valid():
			new_message = form.save(commit=False)
			new_message.chatroom = chatroom

			#associating new messages with current user
			new_message.owner = request.user

			new_message.save()
			return redirect('chat_app:chatroom',chatroom_id = chatroom_id)

	context = {'chatroom':chatroom, 'form':form}
	return render(request, 'chat_app/new_message.html', context)

@login_required
def edit_message(request, message_id):
	"""edit message"""
	message = Message.objects.get(id=message_id)
	chatroom = message.chatroom
	if message.owner != request.user:
		raise Http404

	if request.method != 'POST':
		# form shows unedited message
		form = MessageForm(instance=message)
	else:
		# change message
		form = MessageForm(instance=message, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('chat_app:chatroom',chatroom_id=chatroom.id)

	context = {'message':message,'chatroom':chatroom, 'form':form}
	return render(request, 'chat_app/edit_message.html',context)
