from django.db import models
from django.urls import reverse


class Friend(models.Model):
    friend_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    nickname = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        result = ''
        if self.nickname == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.nickname)
        return result

    def get_absolute_url(self):
        return reverse('aboutme:friend_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('aboutme:friend_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('aboutme:friend_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['last_name', 'first_name', 'nickname']
        unique_together = (('last_name', 'first_name', 'nickname'),)