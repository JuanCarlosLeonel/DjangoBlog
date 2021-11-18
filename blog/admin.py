from django.contrib import admin
from .models import Post, Title


class PostAdmin(admin.ModelAdmin):
    list_display  = ['title', 'author', 'created_at', 'updated_at', 'status']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
admin.site.register(Title)