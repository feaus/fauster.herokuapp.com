from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=100, default=None, help_text="To be displayed in the homepage.")
    thumb = models.ImageField(default='default.png', blank=True, help_text="To be displayed in the homepage.")
    html_class = models.CharField(max_length=100, blank=True, null=True, default=None, help_text="For HTML. Should be "
                                                                                                 "'elemnt'+number")

    def __str__(self):
        return self.title


class Images(models.Model):
    title = models.CharField(max_length=100, default=None, help_text="Won't be displayed.")
    thumb = models.ImageField(default='default.png', blank=True, help_text="To be displayed in the homepage.")

    def __str__(self):
        return self.title