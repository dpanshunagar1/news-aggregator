from home.models import Article

CATEGORY_API_URLS = {
    "India": "https://api.example.com/india",
    "World": "https://api.example.com/world",
    "Local": "https://api.example.com/local",
    "Business": "https://api.example.com/business",
    "Technology": "https://api.example.com/technology",
    "Entertainment": "https://api.example.com/entertainment",
    "Sports": "https://api.example.com/sports",
    "Science": "https://api.example.com/science",
    "Health": "https://api.example.com/health",
}

# utils.py
BASE_API_URL = "https://newsapi.org/v2/everything?q={category}&apiKey=77ce9434280f4f0bae6e39a1214bb1ae"

def get_api_url_by_category(category):
    """Fetch the API URL based on category."""
    return BASE_API_URL.format(category=category)


