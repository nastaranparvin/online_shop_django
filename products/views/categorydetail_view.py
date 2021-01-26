from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, generics, filters, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models.category import Category
from products.serializers.category_serializer import CategorySerializer, CategoryUpdateSerializer
from products.views.prodect_view import LargeResultsSetPagination


class CategoryDetailViews (APIView):
    permission_classes = (AllowAny,)

    def get_object (self,pk):

        try:
            return Category.objects.get(id=pk)
        except Category.DoesNotExist:
            raise Http404


    def get(self,request,pk):
        category_obj= self.get_object(pk)
        serializer= CategorySerializer(instance=category_obj,context={"request":request})
        return Response (serializer.data)


    def put(self,request,pk):
        category_obj= self.get_object(pk)
        serializer= CategoryUpdateSerializer(instance=category_obj ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,400)


    def delete(self,request,pk):
        category_obj=self.get_object(pk)
        category_obj.delete()
        return Response()

class CategoryDetailViews3(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
# orrr class CategoryDetailViews3(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # pagination_class = LargeResultsSetPagination
    # # filter_backends = [DjangoFilterBackend]
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['name', ]
    # # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', ]



    def get(self,request,pk,*args, **kwargs):
        return self.retrieve(request,pk,*args, **kwargs)


    def put(self, request, pk,*args, **kwargs):
        partial = kwargs.pop('partial', False)
        try:
            instance= Category.objects.get(id=pk)
        except Category.DoesNotExist:
            instance = None
        if instance is None:
            return Response(status=404)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    ## (or) return self.update(request, pk, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        # instance = self.get_object()
        # self.perform_destroy(instance)
        # return Response(status=status.HTTP_204_NO_CONTENT)

        return self.destroy(request, pk, *args, **kwargs)




