from django.db import models

from csi_localhost.game.models import Question
from csi_localhost.user_profile.models import Profile


class Response(models.Model):
    CHOICES = ((1, "Correct Answer"), (0, "Wrong Answer"))
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    status = models.PositiveSmallIntegerField(choices=CHOICES, default=1)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer
