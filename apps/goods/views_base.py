import json

from django.http import HttpResponse
from django.views.generic.base import View

from .models import Goods


class GoodsListView(View):
       """
       商品列表
       """
       def get(self,request):
           json_list = []
           goods = Goods.objects.all()[:10]
           for good in goods:
               json_dict = {}
               json_dict["name"] = good.name
               json_dict["category"] = good.category
               json_dict["market_price"] = good.market_price
               json_list.append(json_dict)

           return HttpResponse(json.dumps(json_list),content_type="application/json")