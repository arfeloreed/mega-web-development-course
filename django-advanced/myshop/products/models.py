from django.db import models


# Create your models here.
# model object for address
class Address(models.Model):
    street = models.CharField(max_length=70)
    zipcode = models.PositiveIntegerField()
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city}"


# model object for Category
class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"


# model object for brand
class Brand(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(blank=True, upload_to="product-brand")
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


# model object for shirt
# class Shirt(models.Model):
#     title = models.CharField(max_length=70)
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
#     price = models.PositiveIntegerField()

#     def __str__(self):
#         return f"{self.title}"


# model object for product
class Product(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    image = models.ImageField(blank=True, upload_to="product-img") #uploat_to assigns a folder for the upload file
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField()
    slug = models.SlugField(blank=True)
    is_bestseller = models.BooleanField(default=False)
    suggestions = models.ManyToManyField("self", blank=True)

    # function for customizing the product object appearance
    def __str__(self) -> str:
        return f"{self.title}"

    # function for adding slug equals to product id when saving
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = self.id
        super().save(*args, **kwargs)


# model objecjt for feedback
class Feedback(models.Model):
    name = models.CharField(max_length=50)
    rating = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.product} - Rating {self.rating}"