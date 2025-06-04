import pytest

from data import TestData
from praktikum.bun import Bun


class TestBun:
    # Проверка корректного названия булочек
    @pytest.mark.parametrize('name, price', [(TestData.BUN_NAME_1, TestData.BUN_PRICE_1),
                                             (TestData.BUN_NAME_2, TestData.BUN_PRICE_2)
                                             ])
    def test_get_name_bun_success(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    # Проверка корректной цены булочек
    @pytest.mark.parametrize('name, price', [(TestData.BUN_NAME_1, TestData.BUN_PRICE_1),
                                             (TestData.BUN_NAME_2, TestData.BUN_PRICE_2)
                                             ])
    def test_get_price_bun_success(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price