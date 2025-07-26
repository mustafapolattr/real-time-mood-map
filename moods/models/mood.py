from django.db import models

class Mood(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('excited', 'Excited'),
        ('stressed', 'Stressed'),
        ('neutral', 'Neutral'),
    ]

    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    message = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mood} at ({self.latitude}, {self.longitude})"
