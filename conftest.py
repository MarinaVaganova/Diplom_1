import pytest

from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from helpers import TestMock
from data import TestData


@pytest.fixture
def db():
    return Database()

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    return Mock(spec=Bun)

@pytest.fixture
def mock_ingredient():
    return Mock(spec=Ingredient)

@pytest.fixture
def mock_filling():
    return TestMock.create_mock_ingredient(TestData.FILLING_NAME, TestData.FILLING_PRICE)

@pytest.fixture
def mock_sauce():
    return TestMock.create_mock_ingredient(TestData.SAUCE_NAME, TestData.SAUCE_PRICE)

@pytest.fixture
def prepared_burger(burger, mock_bun, mock_sauce, mock_filling):
    mock_bun.get_price.return_value = TestData.BUN_PRICE_1
    mock_bun.get_name.return_value = TestData.BUN_NAME_1
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_filling)
    return burger