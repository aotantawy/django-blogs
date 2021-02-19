# Generated by Django 3.1.5 on 2021-02-19 13:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('views', models.IntegerField()),
                ('author', models.ManyToManyField(blank=True, related_name='blogs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
