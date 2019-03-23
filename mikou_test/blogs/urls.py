from django.contrib.auth.decorators import login_required
from django.urls import path
from blogs import views

urlpatterns = [
    path('createpost/', login_required(views.MessageCreateView.as_view()), name='createpost'),
    path('last_20_posts/', views.ViewLast20Posts.as_view(), name='last_20_posts'),
    path('posts_by_user/', views.ViewAllPostsByUser.as_view(), name='posts_by_user'),
]
