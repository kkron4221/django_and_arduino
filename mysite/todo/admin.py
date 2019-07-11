from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('message', 'created_date',)
    list_display_links = ('message', 'created_date',)

admin.site.register(Post, PostAdmin)
    
