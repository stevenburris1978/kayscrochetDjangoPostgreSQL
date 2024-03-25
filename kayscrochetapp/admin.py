from django import forms
from django.contrib import admin
from .models import Choice, Item, LikeItem, Customerorder
from django.core.exceptions import ValidationError


admin.site.site_header = "Kay's Crochet Administration"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError("Price cannot be a negative number. Please enter a valid price.")
        return price


class ItemAdmin(admin.ModelAdmin):
    form = ItemForm
    fieldsets = [
        (None, {"fields": ["item_title", "description", "image", "image2", "image3", "image4",
                           "price", "is_sold", "total_quantity", "is_preorder", "preorder_time"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["item_title", "description", "price", "is_sold", "total_quantity", "is_preorder", "preorder_time", "pub_date",
                    "was_published_recently"]
    list_filter = ["pub_date", "is_sold"]
    search_fields = ["item_title"]


class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'street', 'city', 'state', 'zip_code', 'total_price', 'item_title')


admin.site.register(Choice)
admin.site.register(Item, ItemAdmin)
admin.site.register(LikeItem)
admin.site.register(Customerorder, CustomerOrderAdmin)
