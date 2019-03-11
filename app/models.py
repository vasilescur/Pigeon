from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


def article_feature_img_path(instance, filename):
    return 'feature_images/article_{0}/{1}'.format(instance.id, filename)


class Article(models.Model):
    headline = models.CharField(max_length=500, blank=False)
    tags = models.ManyToManyField(Tag)
    text = models.TextField(blank=True, null=True, editable=True)

    feature_image = models.ImageField(upload_to=article_feature_img_path, null=True, blank=True)

    date_created = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)    # Keep articles of deleted users!
    
    is_featured = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.headline

    @property
    def card_desc(self):
        return ' '.join(self.text.split(' ')[:25]) + '...'

    class Meta:
        ordering = ('date_created',)
