from django.contrib import admin
from .models import Category, Tag, Post, About, Link
# Register your models here.
admin.site.site_header = "Administración del blog"
admin.site.index_title = "Panel de control"
admin.site.site_title = 'Blog'

#CATEGORÍAS 
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active', 'created')

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active', 'created')

admin.site.register(Tag, TagAdmin)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','category', 'author', 'published', 'created', 'PostTags')
    ordering = ('author', '-created')
    search_fields = ('title', 'author__username',)
    list_filter = ('author', 'category', 'tags',)

    def PostTags(self, object):
        return ' - '.join([t.name for t in object.tags.all().order_by('name')])
    
    PostTags.short_description = 'Etiquetas'

admin.site.register(Post, PostAdmin)

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('description', 'created')

admin.site.register(About, AboutAdmin)

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('key', 'name', 'url', 'icon')

admin.site.register(Link, LinkAdmin)