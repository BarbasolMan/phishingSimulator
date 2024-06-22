# models.py
from django.db import models

class PhishingEmailTemplate(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
