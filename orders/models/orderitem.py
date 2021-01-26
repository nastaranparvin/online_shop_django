from django.db import models
from django.utils.translation import ugettext_lazy as _

class OrderItem(models.Model):

    order   =models.ForeignKey(to="orders.Order" , on_delete=models.CASCADE , verbose_name= _("Order"))
    product =models.ForeignKey(to="products.Product" , on_delete=models.CASCADE ,verbose_name= _("Product") )
    name    =models.CharField(max_length=20,verbose_name= _("Name"))
    price   =models.PositiveBigIntegerField(verbose_name= _("Price"))
    off     =models.PositiveBigIntegerField(verbose_name= _("Off"))
    quantity=models.PositiveBigIntegerField(verbose_name=_("Quantity"))
    created_at = models.DateTimeField(blank=True,null=True,auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def __str__(self):
        return self.product.name