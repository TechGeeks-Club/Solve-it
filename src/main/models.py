from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os,random,string


# DB_digrame: #? https://drawsql.app/teams/django-34/diagrams/db


# class Competition(models.Model):
#     name = models.CharField(max_length=254)
#     start = models.DateTimeField(default = timezone.now)
#     end = models.DateTimeField(default = timezone.now)
    
#     def __str__(self) -> str:
#         return self.name

class Participant(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    team = models.ForeignKey('Team',on_delete=models.SET_NULL,null=True) #Team_id
    def __str__(self) -> str:
        return f"{self.user.username} ({self.team.name or 'No Team'})"

class Team(models.Model):
    name = models.CharField(max_length=254)
    pin  = models.IntegerField() # we will make it decimal based for now 

    # total= models.GeneratedField(expression, output_field, db_persist=None, **kwargs) 
    
    def __str__(self) -> str:
        return self.name


class QuestionLevel(models.Model):
    level = models.CharField(max_length=20)
    def __str__(self) -> str:
        return f"{self.level}"
    
def upload_question_file(instance:"TestFile", filename):
    print("instance : " , instance)
    return  os.path.join('questions',str(instance.question.level.id),str(instance.question.id),"test.c")
    
def upload_question_h_file(instance:"TestFile", filename):
    return  os.path.join('questions',str(instance.question.level.id),str(instance.question.id),"sol.h")


class TestFile(models.Model):
    question = models.OneToOneField("Question",on_delete=models.CASCADE,null=True,blank=True)
    file     = models.FileField(upload_to=upload_question_file,null=True,blank=True)
    header   = models.FileField(upload_to=upload_question_h_file,null=True,blank=True)
    def __str__(self) -> str:
        return f'ID: {self.id} - Q: {self.question} - PATH: {self.file}'


class Question(models.Model):
    title     = models.CharField(max_length=255,db_default="No Title")
    text      = models.TextField(null=True,blank=True)
    points    = models.IntegerField(db_default=0)
    template  = models.TextField(null=True,blank=True) #contains the path of the template
    date      = models.DateTimeField(default = timezone.now)    
    level     = models.ForeignKey(QuestionLevel,on_delete=models.SET_NULL,null=True)
    is_active = models.BooleanField(default=True)
    # test_num = models.GeneratedField(expression, output_field, db_persist=None, **kwargs)
    
    def __str__(self) -> str:
        return f'id: {self.id} - lvl: {self.level} - ttl: {self.title}'
    
        

# class Test(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     input    = models.TextField()
#     output   = models.TextField()
#     def __str__(self):
#         return f'{self.id} - {self.question} - [ {self.input} ]'
    
    

def upload_answer_to(instance, filename):
    # ran : random string to make sure the file name is unique if the user uploads more than one answer (we will make about 3 attempts)
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4) )

    return  os.path.join('responses',str(instance.participant.team.id),str(instance.question.id),ran,"sol.c")

class Answer(models.Model):
    question   = models.ForeignKey(Question,on_delete=models.CASCADE)#Quetion_id
    participant= models.ForeignKey(Participant,on_delete=models.CASCADE,null=True)    #Team_id
    answer     = models.FileField(upload_to=upload_answer_to,null=True,blank=True)
    # class Meta:
    #     unique_together = [['question', 'Participant']]
        
    def __str__(self) -> str:
        return f'{self.id} - {self.participant} - {self.question}'


class AnswerResault(models.Model):
    answer  = models.ForeignKey(Answer,on_delete=models.CASCADE)
    success = models.IntegerField() # gen field
    # faulure = total - success
    points   = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.id} - {self.answer} - {self.points}'

