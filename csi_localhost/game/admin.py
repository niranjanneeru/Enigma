from django.contrib import admin

from .models import Question, Meme

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question', 'answer']
    list_display = ['question', 'marks', 'answer']
    list_filter = ['marks']


class MemeAdmin(admin.ModelAdmin):
    search_fields = ['content']
    list_display = ['content', 'category']
    list_filter = ['category']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Meme, MemeAdmin)
