from dict_utiliTZ.dict_utiliTZ import select_subkeys, obj_from_dict

'Tests for select_subkeys'


def test_select_subkeys_basic():
    d = {'meal': 'breakfast', 'entree': {'sweet': 'waffle', 'savory': 'eggs'}}
    ks = 'sweet'

    dl, flattened = select_subkeys(d, ks)

    assert dl['entree'] == 'waffle'
    assert flattened is True


def test_select_subkeys_flat():
    d = {'meal': 'breakfast', 'entree': 'waffle'}
    ks = 'sweet'

    dl, flattened = select_subkeys(d, ks)

    assert dl == d
    assert flattened is False


'Test for obj_from_dict'


def test_obj_from_dict_basic_flat():
    class Meal:
        def __init__(self, meal, entree):
            self.name = meal
            self.entree = entree

    d = {'meal': 'breakfast', 'entree': 'waffle'}

    meal = obj_from_dict(Meal, d)

    assert meal.name == 'breakfast'
    assert meal.entree == 'waffle'
