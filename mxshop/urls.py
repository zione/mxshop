"""mxshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include

import xadmin
xadmin.autodiscover()


from xadmin.plugins import xversion
xversion.register_models()
from mxshop.settings import MEDIA_ROOT
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
import  DjangoUeditor

from goods.views import GoodsListViewSet, CategoryViewSet, BannerViewSet, IndexCategoryViewset
from users.views import SmsCodeViewset,UserViewset
from trade.views import ShoppingCartViewset,OrderViewset, AlipayView
from user_operation.views import UserFavViewset, LeavingMessageViewset,AddressViewset

router = DefaultRouter()

#配置goods的url
router.register('goods', GoodsListViewSet, base_name='goods')
#配置Category的url
router.register('categorys', CategoryViewSet, base_name='categorys')
# 短信验证码发送
router.register('codes', SmsCodeViewset, base_name='codes')
router.register('users', UserViewset, base_name='users')
# 收藏
router.register('userfavs', UserFavViewset, base_name='userfavs')
# 留言
router.register('messages', LeavingMessageViewset, base_name='message')
# 收货地址
router.register('address', AddressViewset, base_name='address')
# 购物车
router.register('shopcarts', ShoppingCartViewset, base_name='shopcarts')
# 订单
router.register('orders', OrderViewset, base_name='orders')
# 轮播图
router.register('banners', BannerViewSet, base_name='banners')
# 首页商品系列数据
router.register('indexgoods', IndexCategoryViewset, base_name='indexgoods')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='暮雪生鲜')),
    path('ueditor/',include('DjangoUeditor.urls')),
    # drf自带token认证模式
    path('api-token-auth/', views.obtain_auth_token),
    #
    path('login/', obtain_jwt_token),
    path('alipay/return/', AlipayView.as_view(), name='alipay'),
    # 第三方登录
    path("", include('social_django.urls',namespace='social'))
]

urlpatterns += static('/media/', document_root=MEDIA_ROOT)  #加上这一行
