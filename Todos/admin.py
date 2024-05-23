from django.contrib import admin

from .models import *


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_name', 'level', 'correct_answer', 'variants_id')


class VariantsAdmin(admin.ModelAdmin):
    list_display = ('variants',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Variants, VariantsAdmin)
