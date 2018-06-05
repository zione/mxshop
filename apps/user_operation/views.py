from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import UserFav, UserLeavingMessage,UserAddress
from .serializers import UserFavSerializer,UserFaveDetailSerializer, LeavingMessageSerializer, AddressSerializer
from apps.utils.permissions import IsOwnerOrReadOnly
# Create your views here.


class UserFavViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin, viewsets.GenericViewSet):

    # def dispatch(self, request, *args, **kwargs):
    #     super(UserFavViewset, self).dispatch(request, *args, **kwargs)
    """
    list:
        用户收藏功能
    retrieve:
        判断某个商品是否已经收藏
    create:
        收藏某个商品
    """
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    lookup_field = "goods_id"

    def get_queryset(self):
        return UserFav.objects.filter(user_id=self.request.user.id)

    def get_serializer_class(self):
        if self.action == "list":
            return UserFaveDetailSerializer
        elif self.action == "create":
            return UserFavSerializer
        return UserFavSerializer


class LeavingMessageViewset(mixins.ListModelMixin,mixins.DestroyModelMixin,mixins.CreateModelMixin,viewsets.GenericViewSet):
    """
    list:
        获取用户留言
    create:
        创建用户留言
    delete：
        删除用户留言
    """
    serializer_class = LeavingMessageSerializer
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)

    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user_id=self.request.user.id)


class AddressViewset(viewsets.ModelViewSet):
    """
    收货地址管理
    list:
        获取收货地址
    update:
        更新收货地址
    create:
        添加收货地址
    delete:
        删除收货地址
    """
    serializer_class = AddressSerializer
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)

    def get_queryset(self):
        return UserAddress.objects.filter(user_id=self.request.user.id)