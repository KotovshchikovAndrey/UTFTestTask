from django.core.management.base import BaseCommand
from food_app.models import Food, FoodCategory


class Command(BaseCommand):
    def handle(self, *args, **options):
        drinks = FoodCategory(name_ru="Напитки", order_id=10)
        drinks.save()

        baking = FoodCategory(name_ru="Выпечка", order_id=20)
        baking.save()

        cereals = FoodCategory(name_ru="Крупа", order_id=30)
        cereals.save()

        Food.objects.create(
            category=drinks,
            name_ru="Кофе",
            description_ru="Горячий напиток",
            cost=100.00,
            code=101,
            internal_code=1001,
            is_publish=True,
        )

        Food.objects.create(
            category=drinks,
            name_ru="Чай",
            description_ru="Напиток из листьев чайного куста",
            cost=80.00,
            code=102,
            internal_code=1002,
            is_publish=True,
        )

        Food.objects.create(
            category=drinks,
            name_ru="Сок",
            description_ru="Свежевыжатый фруктовый сок",
            cost=120.00,
            code=103,
            internal_code=1003,
            is_publish=False,
        )

        Food.objects.create(
            category=baking,
            name_ru="Хлеб",
            description_ru="Свежий хлеб",
            cost=50.00,
            code=201,
            internal_code=2001,
            is_publish=False,
        )

        Food.objects.create(
            category=baking,
            name_ru="Булочка",
            description_ru="Сдобная булочка",
            cost=30.00,
            code=202,
            internal_code=2002,
            is_publish=False,
        )

        Food.objects.create(
            category=baking,
            name_ru="Круассан",
            description_ru="Французский круассан",
            cost=40.00,
            code=203,
            internal_code=2003,
            is_publish=False,
        )
