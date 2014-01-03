from django.db import models
from myuser.models import MyUser
from market.models import Listing

# Create your models here.

class PM(models.Model):
    listing = models.ForeignKey(Listing,null=True, blank=True, verbose_name='listing')
    subject = models.CharField('Subject', max_length=140)
    body = models.TextField('Message body')
    sender = models.ForeignKey(MyUser,related_name='sent_pm', verbose_name='Sender')
    recipient = models.ForeignKey(MyUser,related_name='received_pm', null=True, blank=True, verbose_name='Recipient')
    parent_pm = models.ForeignKey('self', related_name='next_pm', null=True, blank=True, verbose_name='Parent PM')
    sent_at = models.DateTimeField('Sent at', null=True, blank=True)
    read_at = models.DateTimeField('Read at', null=True, blank=True)
    replied_at= models.DateTimeField('Replied at', null=True, blank=True)
    sender_deleted_at = models.DateTimeField('Sender deleted at', null=True, blank=True)
    recipient_deleted_at= models.DateTimeField('Recipient deleted at', null=True, blank=True)


