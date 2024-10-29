from django.db import models
import string
import random

class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_unique_short_url()

        super().save(*args, **kwargs)
    
    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for i in range(10))
        return short_url
    
    def generate_unique_short_url(self):
        while True:
            short_url = self.generate_short_url()
            if not URL.objects.filter(short_url=short_url).exists():
                return short_url