from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from uuslug import slugify


class Album(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='album',
        verbose_name='album poster',
    )

    url = models.URLField(blank=True)
    slug = models.SlugField(max_length=500, blank=True)

    title = models.CharField(max_length=300, verbose_name="title")
    description = models.TextField(blank=True, verbose_name='description')
    image = models.ImageField(upload_to='image/album/%Y%m%d', blank=True, null=True)
    created = models.DateField(auto_now_add=True, db_index=True)

    total_likes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Photo Booth'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Album, self).save(*args, **kwargs)

    def increase_comments(self):
        self.total_likes += 1
        self.save(update_fields=['total_likes'])

    def get_absolute_url(self):
        return reverse('album:album_list')
