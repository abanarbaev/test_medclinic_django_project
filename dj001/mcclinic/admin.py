# Register your models here.

from django.contrib import admin
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id" ,"title", "updated", "timestamp"]
    list_display_links = ["id", "updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "text"]
    class Meta:
        model = Post
 
admin.site.register(Post, PostModelAdmin)