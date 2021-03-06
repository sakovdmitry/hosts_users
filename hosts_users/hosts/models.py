from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Hosts(models.Model):
    RESOURCE_CHOICE = [
        ('Win', 'Windows'),
        ('Unix', 'Unix'),
        ('SQL', 'SQL')
    ]
    ip = models.GenericIPAddressField()
    port = models.CharField(max_length=5)
    resource = models.CharField(max_length=10, choices=RESOURCE_CHOICE)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='hosts',
    )
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date',)
