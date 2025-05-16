from django.contrib import admin
from content_app import models

admin.site.register(models.Content)
admin.site.register(models.Playlist)

