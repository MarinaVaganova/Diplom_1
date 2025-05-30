import pytest

from data import TestData
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:
    # Проверка корректности цены ингредиента
    @pytest.mark.parametrize('ingredient_type, name, price', [
        (INGREDIENT_TYPE_SAUCE, TestData.SAUCE_NAME, TestData.SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING, TestData.FILLING_NAME, TestData.FILLING_PRICE)
    ])
    def test_get_price_ingredient_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    # Проверка корректности названия ингредиента
    @pytest.mark.parametrize('ingredient_type, name, price', [
        (INGREDIENT_TYPE_SAUCE, TestData.SAUCE_NAME, TestData.SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING, TestData.FILLING_NAME, TestData.FILLING_PRICE)
    ])
    def test_get_name_ingredient_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    # Проверка корректности типа ингредиента
    @pytest.mark.parametrize('ingredient_type, name, price', [
        (INGREDIENT_TYPE_SAUCE, TestData.SAUCE_NAME, TestData.SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING, TestData.FILLING_NAME, TestData.FILLING_PRICE)
    ])
    def test_get_type_ingredient_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type