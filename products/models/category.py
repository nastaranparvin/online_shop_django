from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):

    name = models.CharField(max_length=20, verbose_name= _ ("Name"))
    image= models.ImageField(upload_to="img/products",null=True,blank=True, verbose_name= _ ("Image") )
    created_at = models.DateTimeField(blank=True,null=True,auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name