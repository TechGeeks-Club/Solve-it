from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os


# DB_digrame: #? https://drawsql.app/teams/django-34/diagrams/db


# class Competition(models.Model):
#     name = models.CharField(max_length=254)
#     start = models.DateTimeField(default = timezone.now)
#     end = models.DateTimeField(default = timezone.now)
    
#     def __str__(self) -> str:
#         return self.name

class Participant(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    team = models.ForeignKey('Team',on_delete=models.CASCADE,null=True) #Team_id
    def __str__(self) -> str:
        return self.user.username

class Team(models.Model):
    name = models.CharField(max_length=254)
    pin  = models.IntegerField(max_length=6) # we will make it decimal based for now 
    # total= models.GeneratedField(expression, output_field, db_persist=None, **kwargs) 
    
    def __str__(self) -> str:
        return self.name


class QuestionLevel(models.Model):
    level = models.CharField(max_length=20)
    def __str__(self) -> str:
        return f"{self.level}"
    
def upload_question_file(instance:"Question", filename):
    return  os.path.join('questions',instance.level,str(instance.id),"test.c")
    
def upload_question_h_file(instance:"Question", filename):
    return  os.path.join('questions',instance.level,str(instance.id),"sol.h")
    
class Question(models.Model):
    question_title = models.CharField(max_length=255,db_default="No Title")
    question_text  = models.TextField(null=True,blank=True)
    points         = models.IntegerField(db_default=0)
    template       = models.TextField() #contains the path of the template
    test_file      = models.FileField(upload_to=upload_question_file,null=True,blank=True)
    sol_h_file     = models.FileField(upload_to=upload_question_file,null=True,blank=True)
    date           = models.DateTimeField(default = timezone.now)    
    level          = models.ForeignKey(QuestionLevel,on_delete=models.CASCADE)
    # test_num = models.GeneratedField(expression, output_field, db_persist=None, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.id} - {self.level} - {self.question_title}'

# class Test(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     input    = models.TextField()
#     output   = models.TextField()
#     def __str__(self):
#         return f'{self.id} - {self.question} - [ {self.input} ]'
    
    

def upload_answer_to(instance, filename):
    return  os.path.join('responses',instance.team.id,instance.question.id,"sol.c")

class Answer(models.Model):
    question   = models.ForeignKey(Question,on_delete=models.CASCADE)#Quetion_id
    Participant= models.ForeignKey(Participant,on_delete=models.CASCADE,null=True)    #Team_id
    answer     = models.FileField(upload_to=upload_answer_to,null=True,blank=True)
    # class Meta:
    #     unique_together = [['question', 'Participant']]
        
    def __str__(self) -> str:
        return f'{self.id} - {self.team} - {self.question}'


class AnswerResault(models.Model):
    answer  = models.ForeignKey(Answer,on_delete=models.CASCADE)
    success = models.IntegerField() # gen field
    # faulure = total - success
    points   = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.id} - {self.answer} - {self.points}'

