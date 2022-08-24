from rest_framework.generics import CreateAPIView
from .serializer import CreateSuggestionSerializer
from .models import Suggestion
from rest_framework.permissions import IsAuthenticated


class CreateSuggestionView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateSuggestionSerializer
    queryset = Suggestion.objects.all()
