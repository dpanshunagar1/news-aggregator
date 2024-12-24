from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)  # Article title
    author = models.CharField(max_length=100, blank=True, null=True)  # Author's name
    source = models.CharField(max_length=100, blank=True, null=True)  # Source of the article
    url = models.URLField(unique=True)  # URL of the article
    content = models.TextField(blank=True, null=True)  # Main content of the article
    published_date = models.DateTimeField(blank=True, null=True)  # Publication date
    added_date = models.DateTimeField(auto_now_add=True)  # Date the article was added to the database
    image_url = models.URLField(blank=True, null=True)  # URL of the article image
    description = models.TextField(blank=True, null=True)  # Description of the article
    source_name = models.CharField(max_length=255, blank=True, null=True)  # Name of the source
    category = models.CharField(max_length=100, blank=True, null=True)  # Category of the article

    def __str__(self):
        return self.title




