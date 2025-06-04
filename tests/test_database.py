import pytest

from data import TestData


class TestDatabase:

    def test_available_buns_success(self, db):
        buns = db.available_buns()
        assert buns[0].name == TestData.BUN_NAME_1


    def test_available_ingredients_success(self, db):
        ingredients = db.available_ingredients()
        assert ingredients[0].name == TestData.SAUCE_NAME
