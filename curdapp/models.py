from django.db import models
from django.contrib.auth.models import User


# Test
class Test(models.Model):
    title = models.CharField(max_length=251)
    slug = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title
    

# Question
class Question(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='quesThumbnails/')
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Option(models.Model):
    option = models.CharField(max_length=100)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.option
    