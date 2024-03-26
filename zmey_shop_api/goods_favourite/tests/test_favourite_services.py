from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.db.models import Prefetch

from goods_favourite.models import Favourite
from goods_favourite.services import favourite_services
from goods.models import Goods


class GoodsFavouriteServicesTestCase(APITestCase):
    """A tests for functions in favourite_services file from services module"""

    def setUp(self):
        self.user = User.objects.create(username="user")
        product = Goods.objects.create(
            name="кардиган",
            main_photo="media/main_photo/name",
            description="Описание товара",
            slug="kardigan",
        )
        Favourite.objects.create(goods=product, user=self.user)

    def test_data_from_get_favourite_goods(self):
        """Ensure we can get correct data from function get_favourite_goods"""

        expected_data = (
            Favourite.objects.filter(user_id=self.user.id)
            .only("goods")
            .prefetch_related(
                Prefetch(
                    "goods",
                    queryset=Goods.objects.only(
                        "id", "name", "main_photo", "description", "slug"
                    ),
                )
            )
        )
        function_data = favourite_services.get_favourite_goods(self.user.id)

        self.assertQuerysetEqual(expected_data, function_data)


