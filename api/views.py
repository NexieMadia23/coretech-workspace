from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import DictionaryTerm, QuizQuestion
from .serializers import DictionaryTermSerializer, QuizQuestionSerializer

# Streaming endpoint for your local dictionary storage
class DictionaryListAPIView(generics.ListAPIView):
    queryset = DictionaryTerm.objects.all().order_by('term')
    serializer_class = DictionaryTermSerializer
    permission_classes = [AllowAny]  # Publicly readable for your mobile app users

# Endpoint to stream randomized quiz review sessions
class QuizQuestionListAPIView(generics.ListAPIView):
    serializer_class = QuizQuestionSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = QuizQuestion.objects.all()
        difficulty = self.request.query_params.get('difficulty', None)
        if difficulty is not None:
            queryset = queryset.filter(difficulty=difficulty)
        # Ordering by '?' completely randomizes the array pool on every single request
        return queryset.order_by('?')[:10]