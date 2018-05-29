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
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from goods.views import GoodsListViewSet, CategoryViewSet

router = DefaultRouter()

#配置goods的url
router.register('goods', GoodsListViewSet, base_name='goods')
#配置Category的url
router.register('categorys', CategoryViewSet, base_name='categorys')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='暮雪生鲜')),
]

urlpatterns += static('/media/', document_root=MEDIA_ROOT)  #加上这一行
