
from django.shortcuts import render
from home.models import NewsArticle


# Create your views here.



# Create your views here.
def home_screen_view(request):
    return render(request, "base.html", {})

def articles_by_category(request, category):
    articles = NewsArticle.objects.filter(category=category)
    return render(request, "home/articles.html", {"articles": articles})

