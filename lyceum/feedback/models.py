__all__ = ["Feedback"]

from django.db import models


class Feedback(models.Model):
    text = models.TextField()
    mail = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
