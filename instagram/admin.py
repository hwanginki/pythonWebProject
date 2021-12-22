from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post

# Register your models here.
# admin.site.register(Post)

@admin.register(Post) # Mapping
# admin.site.register(Post, PostAdmin)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public','created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}"style="width: 72px;" />')
        return None

    def message_length(self, post):
        return f"{len(post.message)} 글자"