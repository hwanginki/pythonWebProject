from django.contrib import admin
from .models import Post

# Register your models here.
# admin.site.register(Post)

@admin.register(Post) # Mapping
# admin.site.register(Post, PostAdmin)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'is_public','created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at']
    search_fields = ['message']
    def message_length(self, post):
        return f"{len(post.message)} 글자"