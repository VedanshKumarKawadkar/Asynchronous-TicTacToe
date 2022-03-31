from django.db import models

# Create your models here.


class Game(models.Model):
    room_code = models.CharField(max_length=15)
    room_creater = models.CharField(max_length=12)
    opponent = models.CharField(max_length=12, blank=True, null=True)
    isOver = models.BooleanField(default=False)