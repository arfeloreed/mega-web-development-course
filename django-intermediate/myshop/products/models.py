from django.db import models


# Create your models here.
# model object for shirt
class Shirt(models.Model):
    title = models.CharField(max_length=70)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title}"


# model object for product
class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    category = models.CharField(max_length=30)
    image = models.ImageField(blank=True, upload_to="product-img") #uploat_to assigns a folder for the upload file
    brand = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    slug = models.SlugField(blank=True)
    is_bestseller = models.BooleanField(default=False)

    # function for customizing the product object appearance
    def __str__(self) -> str:
        return f"{self.title}"

    # function for adding slug equals to product id when saving
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = self.id
        super().save(*args, **kwargs)
