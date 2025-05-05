from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
