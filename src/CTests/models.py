from django.db import models
from django.utils import timezone

class QuestionLevel(models.Model):
    level = models.CharField(max_length=20)
    def __str__(self):
        return self.level


class Qustion(models.Model):
    question_title = models.CharField(max_length=200,db_default="No Title")
    question_text  = models.TextField()
    pub_date       = models.DateTimeField(default = timezone.now)
    points         = models.IntegerField(db_default=0)
    code_tmplate   = models.TextField() # todo: syntax highlighting for this field (in html)
    level          = models.ForeignKey(QuestionLevel, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.id} - {self.level} - {self.question_title}'
    
    
class Test(models.Model):
    question = models.ForeignKey(Qustion, on_delete=models.CASCADE)
    input    = models.TextField()
    output   = models.TextField()
    
    def __str__(self):
        return f'{self.id} - {self.question} - [ {self.input} ]'

class Response(models.Model):
    question  = models.ForeignKey(Qustion, on_delete=models.CASCADE)
    user      = models.CharField(max_length=200)
    user_code = models.TextField()
    score     = models.IntegerField(default=0)
    pub_date  = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return f'{self.id} - {self.user} - {self.question} - {self.score}'
    

# class TreamResponse()