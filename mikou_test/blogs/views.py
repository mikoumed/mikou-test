from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Message
from django.contrib.auth.models import User
from .forms import MessageModelForm
from django.urls import reverse_lazy

class MessageCreateView(CreateView):
    Model = Message
    template_name = 'blogs/create_post.html'
    form_class = MessageModelForm
    success_url = reverse_lazy('index')
    queryset = Message.objects.all()


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MessageCreateView, self).form_valid(form)


class ViewLast20Posts(ListView):
    template_name = 'blogs/list_last_20_posts.html'
    queryset = Message.objects.order_by('-created_at')[:20]


class ViewAllPostsByUser(ListView):
    template_name = 'blogs/all_posts_by_user.html'
    queryset = User.objects.prefetch_related('message_set').all()
