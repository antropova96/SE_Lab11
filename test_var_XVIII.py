from var_XVIII import count_survivors

data = [
    ['', '0', '', '', '', '54', '', '', '', '', '', 'S'],
    ['', '1', '', '', '', '24', '', '', '', '', '', 'S'],
    ['', '0', '', '', '', '45', '', '', '', '', '', 'S'],
    ['', '1', '', '', '', '12', '', '', '', '', '', 'C'],
    ['', '1', '', '', '', '75', '', '', '', '', '', 'C'],
    ['', '0', '', '', '', '33', '', '', '', '', '', 'C'],
    ['', '0', '', '', '', '22', '', '', '', '', '', 'Q'],
]


def test_count_survivors():
    filter = 100
    result = count_survivors(data, filter)

    assert result == {
        'Пункт посадки': ['Саутгемптон', 'Квинстаун', 'Шербур'],
        'Доля выживших': [33, 0, 67],
    }


def test_count_survivors_empty():
    filter = 100
    result = count_survivors([], filter)

    assert result == {
        'Пункт посадки': ['Саутгемптон', 'Квинстаун', 'Шербур'],
        'Доля выживших': [0, 0, 0],
    }


def test_count_survivors_filter():
    filter = 25
    result = count_survivors(data, filter)

    assert result == {
        'Пункт посадки': ['Саутгемптон', 'Квинстаун', 'Шербур'],
        'Доля выживших': [100, 0, 100],
    }
