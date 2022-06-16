from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=32)
    user_age = models.IntegerField(default=0)


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date de publication')



