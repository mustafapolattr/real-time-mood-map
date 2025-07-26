from django.contrib import admin

# Register your models here.
from django.contrib import admin
from moods.models import Mood

admin.site.register(Mood)
