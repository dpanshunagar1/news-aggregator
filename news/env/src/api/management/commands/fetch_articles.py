import requests
from datetime import timedelta
from django.utils import timezone
from api.models import WorldArticle, IndiaArticle, LocalArticle, BusinessArticle, TechnologyArticle, EntertainmentArticle, SportsArticle, HealthArticle, GenericArticle
from django.core.cache import cache


def fetch_and_clean_articles(category):
    cache_key = 'articles_cache'
    cached_data = cache.get(cache_key)

    if cached_data:
        return cached_data
    # API endpoint to fetch articles (replace with your actual API URL)
    api_url = 'https://newsapi.org/v2/everything?q={category}&apiKey=77ce9434280f4f0bae6e39a1214bb1ae'
    
    response = requests.get(api_url)
    if response.status_code != 200:
        return
    

    articles = response.json()

    cache.set(cache_key, articles, timeout=1800)


    for article_data in articles:
        # Determine the category and source based on article data
        category = article_data.get('category', 'Generic')
        source_name = article_data.get('source_name', 'Generic Source')

        # Based on category, save the article to the appropriate model
        model = None
        if category == 'World':
            model = WorldArticle
        elif category == 'India':
            model = IndiaArticle
        elif category == 'Local':
            model = LocalArticle
        elif category == 'Business':
            model = BusinessArticle
        elif category == 'Technology':
            model = TechnologyArticle
        elif category == 'Entertainment':
            model = EntertainmentArticle
        elif category == 'Sports':
            model = SportsArticle
        elif category == 'Health':
            model = HealthArticle
        else:
            model = GenericArticle

        # Create or update the article if it doesn't already exist (based on URL)
        article, created = model.objects.get_or_create(
            url=article_data['url'],
            defaults={
                'title': article_data.get('title', ''),
                'author': article_data.get('author', ''),
                'content': article_data.get('content', ''),
                'published_date': article_data.get('published_date'),
                'image_url': article_data.get('image_url', ''),
                'description': article_data.get('description', ''),
                'category': category,
                'source_name': source_name
            }
        )

        # Clean the database - remove articles with missing or duplicate URLs
        model.objects.filter(url__isnull=True).delete()  # Clean articles with no URL
        model.objects.exclude(url__in=[article_data['url']]).filter(title=article_data['title']).delete()  # Remove duplicate based on title

    # Perform any other necessary cleaning (e.g., cleaning categories with no articles)
    clean_database()


def clean_database():
    # Perform cleaning operations across all models
    models = [WorldArticle, IndiaArticle, LocalArticle, BusinessArticle, TechnologyArticle, EntertainmentArticle, SportsArticle, HealthArticle, GenericArticle]

    for model in models:
        # Clean up articles with missing or invalid URLs
        model.objects.filter(url__isnull=True).delete()
        model.objects.filter(content__isnull=True).delete()  # Remove articles with no content

        # Optionally remove articles that have not been updated in a long time
        cutoff_date = timezone.now() - timedelta(days=30)
        model.objects.filter(published_date__lt=cutoff_date).delete()
