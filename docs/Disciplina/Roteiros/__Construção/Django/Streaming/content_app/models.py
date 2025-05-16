from django.db import models
from django.contrib.auth.models import User

class Content(models.Model):
    CONTENT_TYPES = [
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    file_url = models.URLField()
    thumbnail_url = models.URLField(blank=True, null=True)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    upload_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    is_public = models.BooleanField(default=True)
    status = models.CharField(max_length=20, default='published')
    creator = models.ForeignKey(User, related_name='contents', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Playlist(models.Model):
    title = models.CharField(max_length=255)  # Título da playlist
    description = models.TextField(blank=True, null=True)  # Descrição opcional da playlist
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')  # Proprietário da playlist
    contents = models.ManyToManyField(Content, related_name='playlists')  # Conteúdos incluídos na playlist
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação
    updated_at = models.DateTimeField(auto_now=True)  # Data de última atualização

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'

    def __str__(self):
        return self.title
    

content = Content.objects.create(
    title="Django Tutorial",
    description="A comprehensive tutorial on Django framework.",
    file_url="https://example.com/videos/django_tutorial.mp4",
    thumbnail_url="https://example.com/thumbnails/django_thumb.jpg",
    content_type="video",
    is_public=True,
    creator_id=1  # Assuming user with ID 1 exists
)