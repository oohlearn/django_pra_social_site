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

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            # 將標題slugigy，變成url友好的模樣
        super().save(*args, **kwargs)
