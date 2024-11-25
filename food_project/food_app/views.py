from django.db.models import Exists, OuterRef, Prefetch

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from food_app.models import Food, FoodCategory
from food_app.serializers import FoodListSerializer


class FoodListView(APIView):
    def get(self, request: Request):
        food_list = FoodCategory.objects.prefetch_related(
            Prefetch(
                "food",
                queryset=Food.objects.filter(is_publish=True),
            )
        ).filter(
            Exists(
                Food.objects.filter(
                    category=OuterRef("pk"),
                    is_publish=True,
                )
            )
        )

        serializer = FoodListSerializer(food_list, many=True)
        return Response(data=serializer.data)
