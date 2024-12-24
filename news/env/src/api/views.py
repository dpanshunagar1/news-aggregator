from django.shortcuts import render
from home.models import Article  # Assuming you have an Article model

def article_list_by_category(request, category):
    # Fetch articles from the database based on the category
    articles = Article.objects.filter(category=category)

    # Pass the articles to the template
    return render(request, 'api/articles.html', {'articles': articles, 'category': category})
