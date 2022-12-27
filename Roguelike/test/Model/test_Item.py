from src.Model.Item import Item

def test_Item1():
    item = Item(10)
    
    assert item._health_point == 10
    assert item._activated == False

    assert item.health_point == 10
    assert item.activated == False

    item.activate()
    assert item.activated == True

    item.deactivate()
    assert item.activated == False
