from django.db import models


class AbstractArticle(models.Model):
    title = models.CharField(max_length=255)  # Article title
    author = models.CharField(max_length=100, blank=True, null=True)  # Author's name
    url = models.URLField(unique=True)  # URL of the article
    content = models.TextField(blank=True, null=True)  # Main content of the article
    published_date = models.DateTimeField(blank=True, null=True)  # Publication date
    added_date = models.DateTimeField(auto_now_add=True)  # Date the article was added to the database
    image_url = models.URLField(blank=True, null=True)  # URL of the article image
    description = models.TextField(blank=True, null=True)  # Description of the article

    class Meta:
        abstract = True  # Marks this model as an abstract base class


class WorldArticle(AbstractArticle):
    category = models.CharField(default="World", max_length=100)  # Category for World news
    source_name = models.CharField(default="World News", max_length=255)  # Source name for World

class IndiaArticle(AbstractArticle):
    category = models.CharField(default="India", max_length=100)  # Category for India
    source_name = models.CharField(default="India News", max_length=255)  # Source name for India

class LocalArticle(AbstractArticle):
    category = models.CharField(default="Local", max_length=100)  # Category for Local news
    source_name = models.CharField(default="Local News", max_length=255)  # Source name for Local

class BusinessArticle(AbstractArticle):
    category = models.CharField(default="Business", max_length=100)  # Category for Business news
    source_name = models.CharField(default="Business News", max_length=255)  # Source name for Business

class TechnologyArticle(AbstractArticle):
    category = models.CharField(default="Technology", max_length=100)  # Category for Technology
    source_name = models.CharField(default="Tech News", max_length=255)  # Source name for Technology

class EntertainmentArticle(AbstractArticle):
    category = models.CharField(default="Entertainment", max_length=100)  # Category for Entertainment
    source_name = models.CharField(default="Entertainment News", max_length=255)  # Source name for Entertainment

class SportsArticle(AbstractArticle):
    category = models.CharField(default="Sports", max_length=100)  # Category for Sports news
    source_name = models.CharField(default="Sports News", max_length=255)  # Source name for Sports

class HealthArticle(AbstractArticle):
    category = models.CharField(default="Health", max_length=100)  # Category for Health news
    source_name = models.CharField(default="Health News", max_length=255)  # Source name for Health

class GenericArticle(AbstractArticle):
    category = models.CharField(max_length=100, blank=True, null=True)  # Custom category for other articles
    source_name = models.CharField(max_length=255, blank=True, null=True)  # Custom source for other articles
