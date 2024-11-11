from django.contrib import admin
from .models import Author, Post, Tag

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    list_filter = ("first_name", "last_name")

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "excerpt", "image_name", "date", "slug", "content", "author")
    list_filter = ("title", "author")
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)
    list_filter = ("caption",)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
