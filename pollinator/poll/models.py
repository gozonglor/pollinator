from __future__ import unicode_literals

from django.db import models


class Question(models.Model):
	title = models.CharField(max_length = 500, unique = True)

	def __str__(self):
		return 'question: %s' % self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    votes = models.IntegerField(default=1)

    def __str__(self):
        return 'answer: %s (quetion %s)' % (self.name, self.question.name)

