from var_IX import count_prices

data = [
    ['', '', '1', '', 'male', '', '', '', '', '100', '', ''],
    ['', '', '1', '', 'male', '', '', '', '', '100', '', ''],
    ['', '', '1', '', 'female', '', '', '', '', '100', '', ''],
    ['', '', '2', '', 'male', '', '', '', '', '50', '', ''],
    ['', '', '2', '', 'male', '', '', '', '', '50', '', ''],
    ['', '', '2', '', 'female', '', '', '', '', '50', '', ''],
    ['', '', '3', '', 'male', '', '', '', '', '25', '', ''],
    ['', '', '3', '', 'male', '', '', '', '', '25', '', ''],
    ['', '', '3', '', 'female', '', '', '', '', '25', '', ''],
    ['', '', '3', '', 'female', '', '', '', '', '25', '', '']
]


def test_count_prices_default():
    answer = count_prices(data, filter=None)
    assert answer == {
        'Класс обслуживания': ['1', '2', '3'],
        'Цена билета': [300.0, 150.0, 100.0],
    }


def test_count_prices_no_male():

    answer = count_prices(data, filter='male')
    assert answer['Цена билета'] == [200.0, 100.0, 50.0]


def test_count_prices_no_female():

    answer = count_prices(data, filter='female')
    assert answer['Цена билета'] == [100.0, 50.0, 50.0]


def test_count_prices_empty():
    data = []
    answer = count_prices(data, filter=None)
    assert answer['Цена билета'] == [0, 0, 0]
