
from django.contrib import admin
from django.urls import path
from home.views import home_view
# from rss.views import rss_article_view
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    # path('category/<str:category>/', rss_article_view, name='articles')
     path('category/<str:category>/', views.article_list_by_category, name='article_list_by_category'),
    
]



