from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Books(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Books'
        verbose_name = 'Book'
