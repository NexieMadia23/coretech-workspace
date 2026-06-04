from django.contrib import admin
from django.urls import path
from api.views import DictionaryListAPIView, QuizQuestionListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # CoreTech Data Delivery Routes
    path('api/dictionary/', DictionaryListAPIView.as_view(), name='api-dictionary'),
    path('api/quiz/', QuizQuestionListAPIView.as_view(), name='api-quiz'),
]