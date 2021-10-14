from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'todos'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
