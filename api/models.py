from django.db import models


class Note(models.Model):
    TAG_CHOICES = [
        ('M', 'Money'),
        ('T', 'Todos'),
        ('R', 'Reminders'),
        ('W', 'Work'),
        ('D', 'Default'),
    ]
    tag = models.TextField(max_length=1, choices=TAG_CHOICES, default='D')
    title = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
