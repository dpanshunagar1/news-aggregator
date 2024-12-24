import random
from django.shortcuts import render
from home.models import Article
import feedparser
import bleach


RSS_FEEDS = [
    'https://feeds.ndtv.com/ndtvnews-top-stories',
    'https://feeds.ndtv.com/ndtvnews-latest',
    'https://feeds.ndtv.com/ndtvnews-trending-news',
    'https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms',
    'https://timesofindia.indiatimes.com/rssfeeds/1221656.cms',
    'https://www.livemint.com/rss/companies',
    'https://indianexpress.com/section/world/feed/',
]

# Create your views here.
def rss_article_view(request, category):
    # Fetch articles from the database
    db_articles = list(Article.objects.filter(category=category).distinct())
    
    

    rss_articles = []
    
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
         
        for entry in feed.entries:
            rss_articles.append({
            'title': entry.get('title', 'No Title'),
            'link': entry.get('link', '#'),
            'summary': bleach.clean(
                entry.get('summary', entry.get('description', 'No Summary')),
                tags=[],  # Allow no tags for plain text or specify allowed tags
                strip=True
            ),
            'source': entry.get('source', 'No Source'),
            'published': entry.get('published', 'No Publication Date'),
            'image': entry.enclosures[0].get('url') if 'enclosures' in entry and entry.enclosures else None
            })

    # Combine database and RSS articles
    all_articles =  rss_articles + db_articles

    # Shuffle the combined list
    random.shuffle(all_articles)

    # Remove duplicates (based on title or link for simplicity)
    seen_titles = set()
    unique_articles = []
    for article in all_articles:
        title = article.title if isinstance(article, Article) else article['title']
        if title not in seen_titles:
            seen_titles.add(title)
            unique_articles.append(article)

    # Render the template
    return render(request, 'rss/rss_articles.html', {
        'articles': unique_articles,  # Limit to 20 articles
        'category': category,
    })
