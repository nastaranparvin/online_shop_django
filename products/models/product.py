from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from products.models.category import Category
from products.models.tag import Tag


class Product(models.Model):

    PRODUCT_SIZES = (
        ("S", _("Small")),
        ("M", _("Medium")),
        ("L", _("Large")),
    )

    tags        = models.ManyToManyField(Tag , verbose_name= _("Tag"))
    category   = models.ForeignKey(Category , on_delete=models.CASCADE , verbose_name= _("Category"))
    name        = models.CharField(max_length=30 , verbose_name= _("Name"))
    shirt_size = models.CharField(max_length=1, choices=PRODUCT_SIZES, null=True, blank=True, default=None,verbose_name=_("Shirt size"))
    description = RichTextField(null=True, blank=True, verbose_name=_("Description"))
    price       = models.PositiveIntegerField(verbose_name= _("Price"))
    off         = models.PositiveIntegerField(verbose_name= _("Off"))
    quantity    = models.PositiveIntegerField(verbose_name= _("Quantity"))
    created_at = models.DateTimeField(blank=True,null=True,auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))


    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")



    def __str__(self):
        return self.name

