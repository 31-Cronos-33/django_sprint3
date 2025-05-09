from django.contrib import admin


from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'slug',
        'is_published',
        'created_at',
    )
    search_fields = (
        'title',
        'slug',
    )
    list_filter = (
        'is_published',
        'created_at',
    )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'is_published',
        'created_at',
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at',
    )
    search_fields = (
        'title',
        'text',
        'location',
    )
    list_filter = (
        'is_published',
        'created_at',
    )
