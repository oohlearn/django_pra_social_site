from django.db import models
from django.conf import settings
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/%y%m%d", blank=True)
    caption = models.TextField(blank=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    create = models.DateField(auto_now_add=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      blank=True,
                                      related_name="posts_liked")

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            # 將標題slugigy，變成url友好的模樣
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    posted_by = models.CharField(max_length=100)

    class Meta:
        ordering = ["created_at"]
        
    def __str__(self) -> str:
        return self.body
    
