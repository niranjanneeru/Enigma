from django.utils.timezone import now

from django.db import models
from django.utils.text import slugify


# Create your models here.
class Question(models.Model):
    upload_to = 'question/'
    question = models.CharField(max_length=500)
    number = models.PositiveSmallIntegerField(unique=True)
    slug = models.SlugField(editable=False, unique=True, max_length=700)
    marks = models.IntegerField()
    image = models.URLField(max_length=1000)
    answer = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question + str(now()))
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.number) + f" {self.question}"


class Meme(models.Model):
    CHOICE = ((1, "Success"), (2, "Fail"), (3, "Patience"), (4, "Congratulations"))
    category = models.PositiveSmallIntegerField(choices=CHOICE, default=1)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content
