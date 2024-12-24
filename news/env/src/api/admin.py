from django.contrib import admin

# Register your models here.
from .models import WorldArticle, IndiaArticle, LocalArticle, BusinessArticle, TechnologyArticle, EntertainmentArticle, SportsArticle, HealthArticle, GenericArticle

admin.site.register(WorldArticle)
admin.site.register(IndiaArticle)
admin.site.register(LocalArticle)
admin.site.register(BusinessArticle)
admin.site.register(TechnologyArticle)
admin.site.register(EntertainmentArticle)
admin.site.register(SportsArticle)
admin.site.register(HealthArticle)
admin.site.register(GenericArticle)
