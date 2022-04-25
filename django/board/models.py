from django.db import models
from django.utils import timezone
from django import forms

# title 필드의 length가 2보다 작으면 검증오류 발생시키는 함수 선언하기
def min_length_2_validator(value):
    if len(value) < 2:
        # ValidataionError 예외를 강제로 발생시킨다
        raise forms.ValidationError('title은 2글자 이상 입력해 주세요!')

class Post(models.Model):
    title = models.CharField(max_length=200, validators=[min_length_2_validator])
    content = models.TextField()
    writer = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title +'(' + str(self.id) + ')'


class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.CharField(max_length=20)
    date = models.DateTimeField()

    def __str__(self):
        return self.title
# Create your models here.
