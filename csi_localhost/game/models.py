import datetime

from django.db import models
from django.utils.text import slugify


# Create your models here.
class Question(models.Model):
    upload_to = 'question/'
    question = models.CharField(max_length=500)
    number = models.PositiveSmallIntegerField(unique=True)
    slug = models.SlugField(editable=False, unique=True)
    marks = models.IntegerField()
    image = models.ImageField(upload_to=upload_to)
    answer = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question + str(datetime.datetime.now()))
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.question


class Meme(models.Model):
    CHOICE = ((1, "Success"), (2, "Fail"), (3, "Patience"), (4, "Congratulations"))
    category = models.PositiveSmallIntegerField(choices=CHOICE, default=1)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content
