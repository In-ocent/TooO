from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class TodoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/todo/{self.id}/"
