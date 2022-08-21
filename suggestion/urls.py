from django.urls import path
from .views import CreateSuggestionView

app_name = 'suggestion'

urlpatterns = [
    path('suggestions/', CreateSuggestionView.as_view(), name='create-suggestion')

]
