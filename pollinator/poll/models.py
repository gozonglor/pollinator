from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
	question_text = models.CharField(max_length = 200, unique = True, default="Some Text")
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return 'question: %s' % self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    votes = models.IntegerField(default=1)

    def __str__(self):
        return 'answer: %s %s' % (self.answer, self.question)