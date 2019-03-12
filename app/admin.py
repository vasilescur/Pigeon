from django.contrib import admin

from .models import Article, Tag


def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)
make_published.short_description = 'Mark selected articles as published'


def make_not_published(modeladmin, request, queryset):
    queryset.update(is_published=False)
make_not_published.short_description = 'Mark selected articles as not published'


def make_featured(modeladmin, request, queryset):
    queryset.update(is_featured=True)
make_featured.short_description = 'Mark selected articles as featured'


def make_not_featured(modeladmin, request, queryset):
    queryset.update(is_featured=False)
make_featured.short_description = 'Mark selected articles as not featured'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['headline', 'creator', 'is_published', 'is_featured']
    actions = [make_published, make_not_published, make_featured, make_not_featured]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass