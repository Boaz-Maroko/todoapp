from django.db import models

# Create your models here.

class Task(models.Model):

    

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    time = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Tasks"
