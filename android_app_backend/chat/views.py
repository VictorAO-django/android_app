from django.shortcuts import render
from rest_framework import generics
from .models import Message, ChatRoom
from .serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticated

# Fetch all messages for a given room
class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        room_name = self.kwargs['room_name']
        room = ChatRoom.objects.get(name=room_name)
        return Message.objects.filter(room=room).order_by('timestamp')

# Post a new message to the chatroom
class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        room_name = self.kwargs['room_name']
        room = ChatRoom.objects.get(name=room_name)
        serializer.save(user=self.request.user, room=room)

# Create your views here.
