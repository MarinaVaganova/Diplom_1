import pytest

from data import TestData


class TestBurger:
    # Проверка добавления только соуса
    def test_add_ingredient_only_sauce_success(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)
        assert burger.ingredients[0].get_name() == TestData.SAUCE_NAME and len(burger.ingredients) == 1

    # Проверка добавления соуса и начинки
    def test_add_ingredient_sauce_and_filling_success(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.ingredients[0].get_name() == TestData.SAUCE_NAME and burger.ingredients[1].get_name() == TestData.FILLING_NAME

    # Проверка удаления 1 ингредиента из 2-х
    def test_remove_ingredient_burger_success(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert burger.ingredients[0].get_name() == TestData.FILLING_NAME and len(burger.ingredients) == 1

    # Проверка перемещения ингредиента
    def test_move_ingredient_burger_success(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0,1)
        assert burger.ingredients[0].get_name() == TestData.FILLING_NAME and burger.ingredients[1].get_name() == TestData.SAUCE_NAME

    # Проверка расчета стоимости бургера
    def test_get_price_burger_success(self, prepared_burger):
        expected_price = TestData.BUN_PRICE_1 * 2 + TestData.SAUCE_PRICE + TestData.FILLING_PRICE
        assert prepared_burger.get_price() == expected_price

    # Проверка чека с информацией о бургере
    def test_get_receipt_burger_success(self, prepared_burger):
        expected_price = TestData.BUN_PRICE_1 * 2 + TestData.SAUCE_PRICE + TestData.FILLING_PRICE
        receipt = prepared_burger.get_receipt()
        assert all([
            TestData.BUN_NAME_1 in receipt,
            TestData.SAUCE_NAME in receipt,
            TestData.FILLING_NAME in receipt,
            f'Price: {expected_price}' in receipt
        ])