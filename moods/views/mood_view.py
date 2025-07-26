from rest_framework.viewsets import ModelViewSet
from moods.models.mood import Mood
from moods.serializers import MoodSerializer


class MoodViewSet(ModelViewSet):
    queryset = Mood.objects.all().order_by('-created_at')
    serializer_class = MoodSerializer
