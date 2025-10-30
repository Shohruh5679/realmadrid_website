from django.db import models

# Real Madrid yangiliklari
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Sovrinlar (kuboklar)
class Trophy(models.Model):
    name = models.CharField(max_length=150)
    year = models.IntegerField()
    image = models.ImageField(upload_to='trophy_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.year})"


# Futbolchilar
class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='player_images/', blank=True, null=True)

    def __str__(self):
        return self.name

