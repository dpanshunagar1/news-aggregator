from django.contrib import admin


class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'source', 'published_at')
    list_filter = ('category', 'source')
    search_fields = ('title', 'summary')

    # Add category and source to the detail view of each article
    fieldsets = (
        (None, {
            'fields': ('title', 'summary', 'category', 'source', 'published_at', 'url', 'image_url')
        }),
    )

