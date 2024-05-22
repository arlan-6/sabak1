from django.db import models


class Post(models.Model):
    title = models.CharField("Title", max_length=200)
    price = models.IntegerField(
        default=0,
        help_text="Price in cents",
    )
    description = models.TextField("Description")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title
