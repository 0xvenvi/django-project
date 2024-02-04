from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title + " , " + self.description


class Backgroundimage(models.Model):
    backgroundhome = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.backgroundhome
