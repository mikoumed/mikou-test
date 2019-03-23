from django.contrib import admin
from .models import Message, HashTag


# Register your models here.
class MessageClass(admin.ModelAdmin):
    readonly_fields = ('created_at', )

admin.site.register(Message, MessageClass)
admin.site.register(HashTag)
