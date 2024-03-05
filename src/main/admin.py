from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Participant)
admin.site.register(Team)
admin.site.register(Question)
admin.site.register(QuestionLevel)
admin.site.register(Answer)
admin.site.register(AnswerResault)