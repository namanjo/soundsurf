# Generated by Django 2.2 on 2020-03-30 01:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=100, unique=True)),
                ('album_artist', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('cover_pic', models.ImageField(upload_to='album_covers')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=100, unique=True)),
                ('song', models.FileField(upload_to='songs')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='appmusic.Album')),
            ],
            options={
                'verbose_name_plural': 'Songs',
            },
        ),
    ]
