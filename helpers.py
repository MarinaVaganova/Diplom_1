from unittest.mock import Mock
from praktikum.ingredient import Ingredient


class TestMock:
    @staticmethod
    def create_mock_ingredient(name, price):
        mock = Mock(spec=Ingredient)
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        return mock