from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import UserFav
from .serializers import UserFavSerializer
from utils.permissions import IsOwnerOrReadOnly
# Create your views here.


class UserFavViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin, viewsets.GenericViewSet):

    # def dispatch(self, request, *args, **kwargs):
    #     super(UserFavViewset, self).dispatch(request, *args, **kwargs)
    """
    用户收藏功能
    """
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    lookup_field = "goods_id"

    def get_queryset(self):
        return UserFav.objects.filter(user_id=self.request.user.id)
