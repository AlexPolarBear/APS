from src.Model.Backpack import Backpack
from src.Model.Item import Item

def test_Backpack1():
    backpack = Backpack()
    item1 = Item(1)
    item2 = Item(2)
    item3 = Item(3)

    backpack.add_item(item1)
    assert backpack.get_item(0) == item1

    backpack.add_item(item2)
    assert backpack.get_item(1) == item2

    backpack.add_item(item3)
    assert backpack.get_item(2) == item3

    assert backpack.get_all_items() == [item1, item2, item3]
