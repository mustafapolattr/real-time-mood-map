# Generated by Django 5.2.4 on 2025-07-22 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood', models.CharField(choices=[('happy', 'Happy'), ('sad', 'Sad'), ('angry', 'Angry'), ('excited', 'Excited'), ('stressed', 'Stressed'), ('neutral', 'Neutral')], max_length=20)),
                ('message', models.TextField(blank=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
