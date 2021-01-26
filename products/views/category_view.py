from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets, mixins, generics, filters
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models.category import Category
from products.models.product import Product
from products.serializers.category_serializer import CategorySerializer
from products.serializers.product_serializer import ProductSerializer
from products.views.prodect_view import LargeResultsSetPagination


class CategoryViews(APIView):
    permission_classes= (AllowAny,)
    def get(self, request):
        serializer= CategorySerializer(instance= Category.objects.all(),many=True, context= {"request": request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        return Response(serializer.errors, 400)


class CategoryViews2(viewsets.ViewSet):
    permission_classes= (AllowAny,)

    def list(self,request, *args,**kwargs):
        serializer = CategorySerializer(instance=Category.objects.all(), many=True, context={"request": request})

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        return Response(serializer.errors, 400)


class CategoryViews3(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
# orrrr class CategoryViews3(generics.ListCreateAPIView):

    permission_classes= (AllowAny,)
    queryset= Category.objects.all()
    serializer_class= CategorySerializer
    pagination_class = LargeResultsSetPagination
    # filter_backends = [DjangoFilterBackend]
    filter_backends = [DjangoFilterBackend , filters.SearchFilter]
    filterset_fields = ['name', ]
    # filter_backends = [filters.SearchFilter]
    search_fields = ['name',]

    def get(self, request, *args,**kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
       # (or) return self.list( request )


    def post(self, request , *args, **kwargs):
        return self.create(request , *args, **kwargs)



class CategoryViews4(viewsets.ModelViewSet):
# orrrr class CategoryViews3(mixins.ListModelMixin,
#                       mixins.CreateModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin,
#                       viewsets.GenericAPIView):
    permission_classes= (AllowAny,)
    queryset= Category.objects.all()
    serializer_class= CategorySerializer
    pagination_class = LargeResultsSetPagination
    # filter_backends = [DjangoFilterBackend]
    filter_backends = [DjangoFilterBackend , filters.SearchFilter]
    filterset_fields = ['name', ]
    # filter_backends = [filters.SearchFilter]
    search_fields = ['name',]

    @action(detail=True , methods=["GET"])
    def products(self,request, pk=None):
        self.filterset_fields = ['name', ]
        self.search_fields = ['name', ]
        queryset = self.filter_queryset(Product.objects.filter(categorey=pk))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ProductSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class CategoryViews5(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class= CategorySerializer
    permission_classes=(AllowAny, )
    queryset = Category.objects.all()
    pagination_class = LargeResultsSetPagination