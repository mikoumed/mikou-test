from blogs.models import Message
from .serializers import  MessageModelSerializer
from rest_framework.viewsets import ModelViewSet


class MessageModelViewSet(ModelViewSet):
    serializer_class = MessageModelSerializer
    queryset = Message.objects.all()
