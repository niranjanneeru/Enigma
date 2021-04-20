from django.conf import settings
from django.db import models

from ..game.models import Question


class Profile(models.Model):
    name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    college = models.CharField(max_length=100)
    marks = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    has_completed = models.BooleanField(default=False)
    last_submission = models.DateTimeField()
    current_question = models.ForeignKey(Question, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Profile"
