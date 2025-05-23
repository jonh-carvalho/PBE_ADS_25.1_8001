from django.contrib import admin
from content_app.models import Content, Playlist


class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','content_type', 'is_public', 'upload_date')
    list_filter = ('content_type', 'is_public', 'upload_date')
    search_fields = ('title', 'description')
    ordering = ['upload_date']
    #fields = ('title', 'description', 'file_url', 'thumbnail_url', 'creator')
    fieldsets = (
    ('Informações Básicas', {'fields': ('title', 'description')}),
    ('Detalhes do Arquivo', {'fields': ('file_url', 'thumbnail_url')}),
    ('Informações do Criador', {'fields': ('creator',)}),
    ('Configurações', {'fields': ('content_type', 'is_public', 'status')}),
)


admin.site.register(Content, ContentAdmin)
admin.site.register(Playlist)

