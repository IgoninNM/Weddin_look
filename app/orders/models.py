from django.db import models
from users.models import User

from django.core.mail import EmailMessage
from django.conf import settings


class Order(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phoneNumber = models.CharField(max_length=64, unique=True, null=False, blank=False)
    basket_history = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order #{self.id}. {self.first_name} {self.last_name}'

