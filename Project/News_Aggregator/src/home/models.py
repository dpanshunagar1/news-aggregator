from django.db import models

class NewsArticle(models.Model):
    CATEGORY_CHOICES = [
        ('technology', 'Technology'),
        ('sports', 'Sports'),
        ('business', 'Business'),
        ('world', 'World'),
        ('politics', 'Politics'),
        ('entertainment', 'Entertainment'),
        ('health', 'Health'),
        ('science', 'Science'),
    ]

    title = models.CharField(max_length=255)
    summary = models.TextField()
    url = models.URLField()
    image_url = models.URLField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    source = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title
