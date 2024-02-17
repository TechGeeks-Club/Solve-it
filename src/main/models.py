from django.db import models
from django.contrib.auth.models import User


# DB_digrame: #? https://drawsql.app/teams/django-34/diagrams/db

class Team(models.Model):
    name = models.CharField(max_length=254)
    Pid  = models.ForeignKey(User,on_delete=models.CASCADE) #participent_id
    pin  = models.IntegerField()
    # total= models.GeneratedField(expression, output_field, db_persist=None, **kwargs) 
    
    def __str__(self) -> str:
        return self.name
    
class Quetions(models.Model):
    question = models.TextField()
    pointes  = models.IntegerField()
    template = models.TextField() #contains the path of the template
    # test_num = models.GeneratedField(expression, output_field, db_persist=None, **kwargs)
    level    = models.ManyToManyField("Levels", through="Question_level") 

    def __str__(self) -> str:
        return self.question

class Levels(models.Model):
    name = models.CharField(max_length=254)
    def __str__(self) -> str:
        return self.name
    
class Tests(models.Model):
    inp     = models.TextField()
    exp_res = models.TextField()
    Qid   = models.ForeignKey(Quetions,on_delete=models.CASCADE)
    
class Responses(models.Model):
    Qid       = models.ForeignKey(Quetions,on_delete=models.CASCADE)#Quetion_id
    Tid       = models.ForeignKey(Team,on_delete=models.CASCADE)    #Team_id
    file_path = models.TextField()
    class Meta:
        unique_together = [['Qid', 'Tid']]

class Responce_result(models.Model):
    Rid     = models.ForeignKey(Responses,on_delete=models.CASCADE)
    sec_test= models.IntegerField()
    # points = models.GeneratedField(expression, output_field, db_persist=None, **kwargs)
    