from django.contrib import admin

from products.models.category import Category
from products.models.product import Product
from products.models.tag import Tag

admin.site.register(Product)
admin.site.register(Tag)
#admin.site.register(Category)

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    row_number = 0

    list_display = ("row", "name", "image")

    def row(self, obj):
        count = Category.objects.all().count()
        if self.row_number < count:
            self.row_number += 1
        else:
            self.row_number = 1  # Reset

        return self.row_number
