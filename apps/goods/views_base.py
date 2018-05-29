
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from django.views.generic.base import View

from .models import Goods


class GoodsListView(View):

    def get(self, request):
        goods = Goods.objects.all()[:10]
        return JsonResponse(serializers.serialize('json',goods),safe=False)