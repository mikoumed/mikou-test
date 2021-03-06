from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Message, HashTag
from django.contrib.auth.models import User
from .forms import MessageModelForm
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class MessageCreateView(CreateView):
    Model = Message
    template_name = 'blogs/create_post.html'
    form_class = MessageModelForm
    success_url = reverse_lazy('index')
    queryset = Message.objects.all()


    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.save()
        content = form.cleaned_data['content']
        hashtags = [slugify(i) for i in content.split() if i.startswith("#")]
        for hashtag in hashtags:
            # if HashTag.objects.filter(name=hashtag).exists():
            #     hashtag_object = HashTag.objects.get(name=hashtag)
            # else:
            #     hashtag_object = HashTag.objects.create(name=hashtag)
            hashtag_object = HashTag.objects.get_or_create(name=hashtag)
            form.instance.hashtag_set.add(hashtag_object)
        return super(MessageCreateView, self).form_valid(form)


class ViewLast20Posts(ListView):
    template_name = 'blogs/list_last_20_posts.html'
    queryset = Message.objects.order_by('-created_at')[:20]


class ViewAllPostsByUser(ListView):
    template_name = 'blogs/all_posts_by_user.html'
    queryset = User.objects.prefetch_related('message_set').all()


class ViewHashtagsList(ListView):
    template_name = 'blogs/hashtags_list.html'
    queryset = HashTag.objects.all()


class ViewMessagesWithHashtag(ListView):
    template_name = 'blogs/messages_with_a_hashtag.html'
    queryset = HashTag.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hashtag = self.kwargs['hash']
        hashtag_object = HashTag.objects.get(name=hashtag)
        messages = hashtag_object.message.all() #queryset
        messages_list = []
        for message in messages:
            splitted_message = message.content.split()
            result = []
            for word in splitted_message:
                if word[0] == '#':
                    #use url template tag
                    link = '<a href=' + '"/messages_with_hashtag/(%3FP'+'{}'.format(word[1:])+'%5Cd+)/$">'+word+'</a>'
                    result.append(link)
                else:
                    result.append(word)
            tweet = ' '.join(result)
            messages_list.append(tweet)
        context['messages_list'] = messages_list
        return context
