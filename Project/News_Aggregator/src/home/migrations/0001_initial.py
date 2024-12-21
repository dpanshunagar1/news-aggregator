# Generated by Django 4.2 on 2024-12-16 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('content', models.TextField(blank=True, null=True)),
                ('category', models.CharField(max_length=100)),
                ('published_at', models.DateTimeField()),
                ('source', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]