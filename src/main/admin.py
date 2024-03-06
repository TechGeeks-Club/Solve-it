from django.contrib import admin
from .models import Participant, Team,TestFile, Question, QuestionLevel, Answer, AnswerResault



class ParticipantInline(admin.TabularInline):
    model = Participant
    extra = 1
    max_num = 4
    
    


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['user', 'team']
    

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'pin']
    inlines = [ParticipantInline]


@admin.register(TestFile)
class TestFileAdmin(admin.ModelAdmin):
    list_display = ['id','question', 'file', 'header']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_title', 'points', 'level']

@admin.register(QuestionLevel)
class QuestionLevelAdmin(admin.ModelAdmin):
    list_display = ['level']

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'Participant']

@admin.register(AnswerResault)
class AnswerResaultAdmin(admin.ModelAdmin):
    list_display = ['id', 'answer', 'success', 'points']
