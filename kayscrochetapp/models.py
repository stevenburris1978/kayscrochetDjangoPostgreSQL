from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# table to add item and its details
class Item(models.Model):
    item_title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='items_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='items_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='items_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='items_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pub_date = models.DateTimeField("date published")
    no_of_likes = models.IntegerField(default=0)
    is_sold = models.BooleanField(default=False)
    total_quantity = models.IntegerField(default=1)
    is_preorder = models.BooleanField(default=False)
    preorder_time = models.CharField(max_length=50, default="", blank=True)

    def decrease_stock(self, quantity):
        self.total_quantity = max(0, self.total_quantity - quantity)
        if self.total_quantity == 0:
            self.is_sold = True
        self.save()

    def __str__(self):
        return self.item_title

    def save(self, *args, **kwargs):
        if not self.preorder_time:
            self.preorder_time = ""
        super().save(*args, **kwargs)

    # order by published recently
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        one_day_ago = now - timezone.timedelta(days=1)

        # Make it timezone-aware
        if timezone.is_naive(self.pub_date):
            self.pub_date = timezone.make_aware(self.pub_date)

        return one_day_ago <= self.pub_date <= now


# table to add choices to vote on of future crocheted items
class Choice(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# table to store likes
class LikeItem(models.Model):
    item_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


# table to store customer order info
class Customerorder(models.Model):
    full_name = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.full_name}'s Order"

    class Meta:
        verbose_name = "Customer_Order"
        verbose_name_plural = "Customer_Orders"
