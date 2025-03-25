import pytest

from src.lawngrass import LawnGrass
from typing import Any


def test_lawngrass_init(grass1: Any) -> None:
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_lawngrass_add(grass1: LawnGrass, grass2: LawnGrass) -> None:
    assert grass1 + grass2 == 35


def test_lawngrass_add_error(grass1: LawnGrass, grass2: LawnGrass) -> None:
    with pytest.raises(TypeError):
        grass1 + 1
