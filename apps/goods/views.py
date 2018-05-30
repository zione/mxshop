
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from goods.serializer import GoodsSerializer, CategorySerializer
from goods.models import Goods,GoodsCategory
from goods.filters import GoodsFilter
# Create your views here.


class StandarResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表
    """
    # authentication_classes = (TokenAuthentication,)
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandarResultsSetPagination
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class = GoodsFilter
    # filter_fields = ('name', 'goods_brief', 'goods_desc')
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')


class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表
    """
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer

