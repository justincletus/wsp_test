from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Test(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
class Questions(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    title = models.ForeignKey(Test, default=None, null=True, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    a1 = models.CharField(max_length=100, default='')
    a2 = models.CharField(max_length=100, default='')
    a3 = models.CharField(max_length=100, default='')
    a4 = models.CharField(max_length=100, default='')
    answer = models.CharField(max_length=200, default='')
    marks = models.IntegerField(default=0)
    
    def __str__(self):
        return self.question
    
    def get_absolute_url(self):
        return reverse("test-details", args=[str(self.id)])


class SubmitedAnswer(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    qusetion = models.ForeignKey(Questions, default=None, null=True, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, default='')
    marks = models.FloatField(null=True, default=0.0)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.answer   
    
