from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os


# DB_digrame: #? https://drawsql.app/teams/django-34/diagrams/db

class Participant(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    team = models.ForeignKey('Team',on_delete=models.CASCADE,null=True) #Team_id
    def __str__(self) -> str:
        return self.user.username

class Team(models.Model):
    name = models.CharField(max_length=254)
    # Pid  = models.ForeignKey(User,on_delete=models.CASCADE) #!false
    pin  = models.CharField(max_length=6) 
    # total= models.GeneratedField(expression, output_field, db_persist=None, **kwargs) 
    
    def __str__(self) -> str:
        return self.name


class QuestionLevel(models.Model):
    level = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.level
    
    
class Question(models.Model):
    question_title = models.CharField(max_length=255,db_default="No Title")
    question_text  = models.TextField()
    points         = models.IntegerField(db_default=0)
    template       = models.TextField() #contains the path of the template
    date           = models.DateTimeField(default = timezone.now)    
    level          = models.ForeignKey(QuestionLevel,on_delete=models.CASCADE)
    # test_num = models.GeneratedField(expression, output_field, db_persist=None, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.id} - {self.level} - {self.question_title}'

    
class Test(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    input    = models.TextField()
    output   = models.TextField()
    def __str__(self):
        return f'{self.id} - {self.question} - [ {self.input} ]'
    
    

def upload_answer_to(instance, filename):
    return  os.path.join('responses',instance.team.id,instance.question.id,filename)

class Answer(models.Model):
    question   = models.ForeignKey(Question,on_delete=models.CASCADE)#Quetion_id
    team       = models.ForeignKey(Team,on_delete=models.CASCADE)    #Team_id
    answer     = models.FileField(upload_to=upload_answer_to)
    class Meta:
        unique_together = [['question', 'team']]
        
    def __str__(self) -> str:
        return f'{self.id} - {self.team} - {self.question}'


class AnswerResault(models.Model):
    answer  = models.ForeignKey(Answer,on_delete=models.CASCADE)
    success = models.IntegerField() # gen field
    # faulure = total - success
    points   = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.id} - {self.answer} - {self.points}'

