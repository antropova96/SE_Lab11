from var_XVIII import count_survivors, prepare_data

data = [
    ['', '0', '', '', '', '54', '', '', '', '', '', 'S'],
    ['', '1', '', '', '', '12', '', '', '', '', '', 'C'],
    ['', '0', '', '', '', '22', '', '', '', '', '', 'Q'],
    ['', '1', '', '', '', '24', '', '', '', '', '', 'S'],
    ['', '1', '', '', '', '75', '', '', '', '', '', 'C'],
    ['', '0', '', '', '', '45', '', '', '', '', '', 'S'],
    ['', '0', '', '', '', '33', '', '', '', '', '', 'C'],
    ['', '0', '', '', '', '20', '', '', '', '', '', 'S'],
    ['', '0', '', '', '', '47', '', '', '', '', '', 'S'],
    ['', '1', '', '', '', '29', '', '', '', '', '', 'S']
]


def test_count_survivors():
    filter = 100
    result = count_survivors(filter, data)

    assert result == {
        'Выживших': [2, 2, 0],
        'Пассажиров': [6, 3, 1],
        'Пункт посадки': ['S', 'C', 'Q']
    }


def test_count_survivors_empty():
    filter = 100
    result = count_survivors(filter, [])

    assert result == {
        'Выживших': [],
        'Пассажиров': [],
        'Пункт посадки': []
    }


def test_count_survivors_filter():
    filter = 25
    result = count_survivors(filter, data)

    assert result == {
        'Выживших': [1, 0, 1],
        'Пассажиров': [1, 1, 2],
        'Пункт посадки': ['C', 'Q', 'S']
    }


def test_prepare_data():
    filter = 100
    passengers = count_survivors(filter, data)
    result = prepare_data(passengers)
    assert result == {
        'Доля выживших': [33, 67, 0],
        'Пункт посадки': ['Саутгемптон', 'Шербур', 'Квинстаун']
    }
 
