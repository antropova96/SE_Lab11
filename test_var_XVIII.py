from var_XVIII import count_survivors, prepare_data

data = [
    ['125', '0', '1', '', 'male', '54', '0', '1', '35281', '77.2875', 'D26', 'S'],
    ['126', '1', '3', '', 'male', '12', '1', '0', '2651', '11.2417', '', 'C'],
    ['127', '0', '3', '', 'male', '22', '0', '0', '370372', '7.75', '', 'Q'],
    ['128', '1', '3', '', 'male', '24', '0', '0', 'C 17369', '7.1417', '', 'S'],
    ['129', '1', '3', '', 'female', '75', '1', '1', '2668', '22.3583', 'F E69', 'C'],
    ['130', '0', '3', '', 'male', '45', '0', '0', '347061', '6.975', '', 'S'],
    ['131', '0', '3', '', 'male', '33', '0', '0', '349241', '7.8958', '', 'C'],
    ['132', '0', '3', '', 'male', '20', '0', '0', 'SOTON/O.Q. 3101307', '7.05', '', 'S'],
    ['133', '0', '3', '', 'female', '47', '1', '0', 'A/5. 3337', '14.5', '', 'S'],
    ['134', '1', '2', '', 'female', '29', '1', '0', '228414', '26', '', 'S']
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