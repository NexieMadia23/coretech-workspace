from django.contrib import admin
from .models import UserProfile, DictionaryTerm, QuizQuestion

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'xp', 'current_streak', 'last_active_date')
    search_fields = ('user__username',)
    list_filter = ('level',)

@admin.register(DictionaryTerm)
class DictionaryTermAdmin(admin.ModelAdmin):
    list_display = ('term', 'category', 'date_added')
    search_fields = ('term', 'definition')
    list_filter = ('category',)

@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text_short', 'difficulty', 'correct_option')
    search_fields = ('question_text', 'explanation')
    list_filter = ('difficulty',)

    # Helper to keep the question text from stretching the table layout
    def question_text_short(self, obj):
        return obj.question_text[:50] + "..." if len(obj.question_text) > 50 else obj.question_text
    question_text_short.short_description = 'Question'