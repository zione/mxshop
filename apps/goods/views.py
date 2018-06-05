
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend

from goods.serializer import GoodsSerializer, CategorySerializer, BannerSerializer, IndexCategorySerializer
from goods.models import Goods,GoodsCategory,Banner
from goods.filters import GoodsFilter
# Create your views here.


class StandarResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
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


class BannerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表
    """
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class IndexCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页商品分类数据
    """
    queryset = GoodsCategory.objects.filter(is_tab=True,name__in=["生鲜食品","酒水饮料"])
    serializer_class = IndexCategorySerializer




