from django.db import models
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage


class Photo(models.Model):
    file = models.ImageField(upload_to='photo', blank=True)


# Photo모델이 삭제되는 시점의 signal을 이용해서
# 인스턴스가 삭제될 때 file필드의 파일도 삭제 하도록 구현
@receiver(pre_delete, sender=Photo)
def model_pres_delete(sender, **kwargs):
    print('Sender: {}'.format(sender))
    print('Pre - Deleted: {}'.format(kwargs['instance'].__dict__))


@receiver(post_delete, sender=Photo)
def model_post_delete(sender, **kwargs):
    print("kwargs['instance'].__dict__['file'] . {}".format(kwargs['instance'].__dict__['file']))
    default_storage.delete(kwargs['instance'].__dict__['file'])
    print('Sender: {}'.format(sender))
    print('Deleted: {}'.format(kwargs['instance'].__dict__))
