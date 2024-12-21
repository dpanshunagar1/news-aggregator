
from django.contrib import admin
from django.urls import path
from home.views import(
    home_screen_view,
    articles_by_category,
    
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view , name="home"),
    path('category/<str:category>/', articles_by_category, name="articles_by_category"),
]
