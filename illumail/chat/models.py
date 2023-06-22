from django.db import models
from users.models import CustomUser


class ChatWithUser(models.Model):
    from_user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='От кого', related_name='from_user')
    to_user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='Кому', related_name='to_user')
    text_message = models.TextField(verbose_name='Текст сообщения')
    date_message = models.DateTimeField(auto_now=True, verbose_name='Дата отправки')

    def __str__(self):
        return f"{self.from_user}"

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

