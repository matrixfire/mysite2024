from django.db import models


class Slide(models.Model):
    img = models.ImageField(upload_to='slides/')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)

    def __str__(self):
        return self.title


