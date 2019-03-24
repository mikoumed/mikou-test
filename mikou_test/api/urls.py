from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()

router.register('messages', views.MessageModelViewSet, base_name='messages')
urlpatterns = []
urlpatterns += router.urls
