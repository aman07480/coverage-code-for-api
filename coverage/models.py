from django.db import models

class APICoverage(models.Model):

    endpoint = models.CharField(max_length=255, unique=True)

    method = models.CharField(max_length=10)

    hit_count = models.IntegerField(default=0)

    last_hit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.endpoint} ({self.hit_count})"