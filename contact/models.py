from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255, null=False)
    number = models.IntegerField(null=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
