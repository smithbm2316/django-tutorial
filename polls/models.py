import datetime

from django.db import models
from django.utils import timezone

from polls.helpers import nanoid

# Create your models here.
class Question(models.Model):
    id = models.TextField(primary_key=True, default=nanoid, editable=False, unique=True)
    question_text = models.TextField()
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self) -> bool:
        """ Checks to see if the question was published within the last 24 hours

        Returns:
            `true` if the `pub_date` field was within the last 24 hours
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    id = models.TextField(primary_key=True, default=nanoid, editable=False, unique=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField()
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
