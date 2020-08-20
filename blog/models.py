from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, help_text="To be displayed in list of articles and in article detail.")
    slug = models.SlugField(help_text="Url.")
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png', blank=True, help_text="To be displayed in article list.")
    thumb = models.ImageField(default='default.png', blank=True, help_text="To be displayed in article detail. Should "
                                                                           "be banner-style (wide).")

    body_0 = models.TextField(default="None", help_text="To be displayed in article detail. First paragraph.")
    body_image_0 = models.ImageField(default='default.png', blank=True, help_text="To be displayed in article detail. "
                                                                                  "First image.")
    body_1 = models.TextField(default="None", help_text="Second paragraph.")
    body_image_1 = models.ImageField(default='default.png', blank=True)
    body_2 = models.TextField(default="None", help_text="Third paragraph.")
    body_image_2 = models.ImageField(default='default.png', blank=True)
    body_3 = models.TextField(default="None", help_text="Fourth paragraph.")
    body_image_3 = models.ImageField(default='default.png', blank=True)
    body_4 = models.TextField(default="None", help_text="Fifth paragraph.")
    body_image_4 = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title