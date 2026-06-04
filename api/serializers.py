from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, DictionaryTerm, QuizQuestion

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'xp', 'level', 'current_streak', 'longest_streak']

class DictionaryTermSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = DictionaryTerm
        fields = ['id', 'term', 'definition', 'category', 'category_display']

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ['id', 'question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option', 'difficulty', 'explanation']