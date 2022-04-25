# Generated by Django 4.0.3 on 2022-04-25 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reccomendations', '0008_spotifyplaylistdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='IMDBMovieData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('googleId', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120)),
                ('image', models.CharField(max_length=255)),
            ],
        ),
    ]
