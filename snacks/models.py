from django.db import models
from django.contrib.auth import get_user_model


class Snack(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # specify ordering for display
        ordering = ["-created_at"]

    def __str__(self):
        # default print representation
        return self.name
