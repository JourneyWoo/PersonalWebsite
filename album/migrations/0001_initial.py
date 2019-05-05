# Generated by Django 2.1.1 on 2019-05-05 00:09

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
                ('url', models.URLField(blank=True)),
                ('slug', models.SlugField(blank=True, max_length=500)),
                ('title', models.CharField(max_length=300, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/album/%Y%m%d')),
                ('created', models.DateField(auto_now_add=True, db_index=True)),
                ('total_likes', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to=settings.AUTH_USER_MODEL, verbose_name='album poster')),
            ],
            options={
                'verbose_name_plural': 'Photo Booth',
                'ordering': ('-created',),
            },
        ),
    ]