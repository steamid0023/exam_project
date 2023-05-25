from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    position = models.PositiveSmallIntegerField(default=0)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="children")
