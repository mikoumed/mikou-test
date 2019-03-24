from rest_framework import serializers
from blogs.models import Message



class MessageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['content']
