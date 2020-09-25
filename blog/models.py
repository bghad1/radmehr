from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('blog:blog_detail',
    #                    args=[self.publish.year,
    #                          self.publish.month,
    #                          self.publish.day, self.slug])


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
