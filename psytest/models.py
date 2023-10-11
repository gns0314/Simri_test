from django.db import models
from user.models import User
# Create your models here.


class PsyTest(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    hit = models.PositiveIntegerField()


class Follow(models.Model):
    psytest = models.ForeignKey(PsyTest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follow = models.PositiveIntegerField()


class Question(models.Model):
    psytest = models.ForeignKey(PsyTest, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=100)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=100)


class Result(models.Model):
    psytest = models.ForeignKey(PsyTest, on_delete=models.CASCADE, related_name='results')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='results')
    result_text = models.CharField(max_length=100)
    result_img = models.ImageField(upload_to='images/')