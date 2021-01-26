from django.contrib import admin
from orders.models.order import Order
from orders.models.orderitem import OrderItem
from django.utils.translation import ugettext_lazy as _

# admin.site.register(Order)
# admin.site.register(OrderItem)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    row_number = 0

    list_display = (
        "row", "number_order", "phone_number", "full_name", "total_price",
    )

    list_display_links = ("number_order",)
    readonly_fields = ("number_order", 'name', 'familly', 'phone_number',"total_price")
    search_fields = ['number_order',  'name', 'familly', 'phone_number',]
    filterset_fields = ['number_order', ]
    inlines = [
        OrderItemInline
    ]

    def full_name(self, obj):
        return f"{obj.name} {obj.familly}"

    full_name.allow_tags = True
    full_name.short_description = _("Full name")

    def row(self, obj):
        count = Order.objects.all().count()
        if self.row_number < count:
            self.row_number += 1
        else:
            self.row_number = 1  # Reset

        return self.row_number

    row.allow_tags = True
    row.short_description = _("Row")



    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False
