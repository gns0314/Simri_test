from django.contrib import admin
from .models import PsyTest, Question, Answer, Result, Follow

# Register your models here.

admin.site.register(PsyTest)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Result)
admin.site.register(Follow)