from django.shortcuts import render
import feedparser
import bleach



# List of RSS feed URLs
RSS_FEEDS = [
    'https://feeds.ndtv.com/ndtvnews-top-stories',
    'https://feeds.ndtv.com/ndtvnews-latest',
    'https://feeds.ndtv.com/ndtvnews-trending-news',
    'https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms',
    'https://timesofindia.indiatimes.com/rssfeeds/1221656.cms',
    'https://www.livemint.com/rss/companies',
    'https://indianexpress.com/section/world/feed/',
]




def home_view(request):
    feeds = []
    
    for feed_url in RSS_FEEDS:

        # Fetch and parse each feed
        feed = feedparser.parse(feed_url)
        if(feed.bozo == 0):
            feeds.append({
            'feed_title': feed.feed.get('title', 'No Title'),
            'entries': [
            {
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
            }
            for entry in feed.entries[:15]  # Get top 5 articles
            ]
            })
            
    return render(request, 'home/home.html' ,{'feeds': feeds})

