
from django.urls import re_path
from rest_framework.routers import DefaultRouter

from products.views.category_view import CategoryViews, CategoryViews2, CategoryViews3, CategoryViews4, CategoryViews5
from products.views.categorydetail_view import CategoryDetailViews, CategoryDetailViews3
from products.views.prodect_view import ProductView

router= DefaultRouter()
router.register("products",ProductView, basename="product_urls")
router.register("categories2",CategoryViews2, basename="category_2")
router.register("categories4",CategoryViews4, basename="category_4")
router.register("categories5",CategoryViews5, basename="category_5")


urlpatterns = [
    re_path(r"categories/?$",CategoryViews.as_view()),
    re_path(r"categories/(?P<pk>\d+)/?$", CategoryDetailViews.as_view()),
    re_path(r"categories3/?$",CategoryViews3.as_view()),
    re_path(r"categories3/(?P<pk>\d+)/?$", CategoryDetailViews3.as_view()),

    # اگر بخوایم میتونیم به شکل زیر ادرس انومات کنگوری 2 رو به صورت دستی بنویسیم
    # re_path(r"categories2/?$",CategoryViews2.as_view({"get" : "list" , "post": "create"})),
    ]

urlpatterns += router.urls
