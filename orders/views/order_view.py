from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.models.order import Order
from orders.models.orderitem import OrderItem
from products.models.product import Product


class OrderView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        exist_quantity= bool
        list_products = []
        total_price = 0
        data = request.data
        if not data:
            return Response(data={"error": "request body is empty"}, status=status.HTTP_400_BAD_REQUEST)
        # اگر دیتا درخواستمون بصورت لیست نبود
        if not isinstance(data, list):
            return Response(data={"error": "request body is empty"}, status=status.HTTP_400_BAD_REQUEST)


        for product in data:

            id = product.get("product_id")
        #     product_obj= Product.objects.get(id=id)
        #     exist_quantity = product_obj.quantity >= quantity
        #     if product_obj and exist_quantity:
        #         list_products.append({"product_obj":product_obj, "quantity": quantity})
        #     else:
        #         print("not found")
        #         Response(status=400)
        # print(list_products)
            try:
                product_obj = Product.objects.get(id=id)
                quantity = product.get("product_quantity")
                exist_quantity= product_obj.quantity >= quantity
                list_products.append({"product_obj": product_obj, "quantity": quantity})
            except Product.DoesNotExist:
                print(list_products)
                return Response(data={"error": f"product with id {id} dont found"}, status=status.HTTP_404_NOT_FOUND)

        # calculate total_price
        for dic in list_products:
            product_obj=dic.get("product_obj")
            quantity=dic.get("quantity")
            pro_price = product_obj.price
            total_price += (pro_price * quantity * ((100 - (product_obj.off)) / 100))

        # creat order
        order_obj = Order.objects.create(
            phone_number=request.user.phone_number,
            name=request.user.first_name,
            familly=request.user.last_name,
            total_price=total_price,
        )

        # creat order_item
        for product_obj,quantity in list_products:
            OrderItem.objects.create(
                order=order_obj,
                product=product_obj,
                name=product_obj.name,
                price=product_obj.price,
                off=product_obj.off,
                quantity=quantity,
            )

        return Response(data={"message": "Successfully your order"}, status=status.HTTP_200_OK)
