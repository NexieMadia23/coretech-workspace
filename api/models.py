from django.db import models
from django.contrib.auth.models import User

# 1. GAMIFICATION: Tracking XP, Levels, and Streaks
class UserProfile(models.Model):  # <--- Double check this line says exactly models.Model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    current_streak = models.IntegerField(default=0)
    longest_streak = models.IntegerField(default=0)
    last_active_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Lvl {self.level} ({self.xp} XP)"

# 2. OFFLINE-FIRST DICTIONARY
class DictionaryTerm(models.Model):
    CATEGORY_CHOICES = [
        ('CS', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('SE', 'Software Engineering'),
        ('NW', 'Networking'),
        ('AI', 'Artificial Intelligence'),
    ]
    
    term = models.CharField(max_length=100, unique=True)
    definition = models.TextField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='IT')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.term

# 3. ARENA: Gamified Quiz Questions
class QuizQuestion(models.Model):
    DIFFICULTY_CHOICES = [
        ('EASY', 'Easy (10 XP)'),
        ('MED', 'Medium (20 XP)'),
        ('HARD', 'Hard (50 XP)'),
    ]
    
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1, help_text="Enter exactly: A, B, C, or D")
    difficulty = models.CharField(max_length=4, choices=DIFFICULTY_CHOICES, default='EASY')
    explanation = models.TextField(blank=True, help_text="Shown to the student after answering.")

    def __str__(self):
        return f"[{self.difficulty}] {self.question_text[:30]}..."