from .models import Message
from celery import shared_task
from django.utils import timezone
from dateutil.relativedelta import relativedelta


@shared_task
def delete_old_message():
    start_date = timezone.localtime(timezone.now())
    end_date = start_date + relativedelta(day=10)
    objects_to_delete = Message.objects.filter(created_at__lt=end_date)
    objects_to_delete.delete()
    return result
