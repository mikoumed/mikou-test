from blogs.models import Message
from .serializers import  MessageModelSerializer
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated


class MessageModelViewSet(ModelViewSet):
    serializer_class = MessageModelSerializer
    queryset = Message.objects.all()

    def get_permissions(self):
        if self.action == 'update' or self.action == 'destroy':
            return [IsOwnerOrReadOnly()]
        return [IsAuthenticated()]
