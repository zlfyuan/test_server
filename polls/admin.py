from django.contrib import admin

from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date','question_text']
    # 拥有数十个字段的表单，你可能更期望将表单分为几个字段集：
    fieldsets = [
        (None,      {'fields':['question_text']}),
        ('Date information',     {'fields':['pub_date'],'classes':['collapse']})
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)

# admin.site.register(Choice)
