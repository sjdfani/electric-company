from rest_framework.generics import CreateAPIView
from .serializer import SuggestionSerializer
from .models import Suggestion
from rest_framework.permissions import IsAuthenticated


class CreateSuggestionView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SuggestionSerializer
    queryset = Suggestion.objects.all()
