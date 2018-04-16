from rest_framework import viewsets
from models import TodoItem
from models import Invitation
from serializers import TodoItemSerializer
from serializers import InvitationSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class TodoItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TodoItems to be CRUDed.
    """
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
class InvitationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Invitation to be CRUDed.
    """
    queryset = Invitation.objects.all()
    serializer_class = InvitationSerializer
    