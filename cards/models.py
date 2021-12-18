from django.db import models


class Card(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="articles/images/", null=True)
    summaryText = models.TextField(max_length=1023, blank=True)
    ingredientsForRecipe = models.TextField(max_length=1000, blank=True)
    directionsForRecipe = models.TextField(max_length=5000, blank=True)
    jumbotronImage = models.ImageField(upload_to="articles/images/", null=True)

    def __str__(self):
        return self.title
