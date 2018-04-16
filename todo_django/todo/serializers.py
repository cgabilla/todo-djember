from rest_framework import serializers
from models import TodoItem
from models import Invitation


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('label', 'text', 'done')

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = ('email', 'first', 'last')
                
