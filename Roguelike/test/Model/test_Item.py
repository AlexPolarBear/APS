from src.Model.Item import Item


def test_Item1():
    item = Item(10)

    assert item._health_point == 10
    assert not item._activated

    assert item.health_point == 10
    assert not item.activated

    item.activate()
    assert item.activated

    item.deactivate()
    assert not item.activated
