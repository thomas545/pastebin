from django.db import models
from core.models import TimeStampedModel
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
User = get_user_model()


class SyntaxHighLight(TimeStampedModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Paste(TimeStampedModel):

    PUBLIC = 'c'
    PRIVATE = 'p'
    STATUS_CHOICES = (
        (PUBLIC, 'public'),
        (PRIVATE, 'private')
    )
    EXPIREATION_CHOICES = (
        ('Never', 'never'),
        ('10m', '10 minute'),
        ('1h', '1hour'),
        ('1day', 'One Day'),
        ('1week', 'One Week'),
        ('2weeks', 'Two Weeks'),
        ('1month', 'One Month'),
    )

    user = models.ForeignKey(User, related_name='pastes', on_delete=models.CASCADE, blank=True, null=True)
    syntax_highlight = models.ForeignKey(SyntaxHighLight, related_name='syntax', on_delete=models.CASCADE)
    paste = models.TextField()
    url = models.URLField(blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default=PUBLIC)
    Expireation = models.CharField(choices=EXPIREATION_CHOICES, max_length=20, default='never')

    def __str__(self):
        return self.paste

    # def save(self):
    #     if not self.url:
    #         self.url = 'http://127.0.0.1:8000/' + self.id
    #     super(Paste, self).save(*args, **kwargs)