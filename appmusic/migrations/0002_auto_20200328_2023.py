# Generated by Django 2.2 on 2020-03-28 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appmusic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songs',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='appmusic.Album'),
        ),
    ]
