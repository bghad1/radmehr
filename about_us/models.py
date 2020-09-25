from django.db import models


class AboutUs(models.Model):
    about_description = models.TextField(max_length=800)
