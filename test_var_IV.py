from var_IV import count_passengers

data = [
        ['', '0', '3', '', '', '22'],
        ['', '1', '1', '', '', '38'],
        ['', '1', '3', '', '', '26'],
        ['', '1', '1', '', '', '61'],
        ['', '0', '3', '', '', '35'],
    ]


def test_count_survived_passengers():
    pclass_filter = 'Любой'
    answer = count_passengers(data, pclass_filter)

    assert answer == {'under_30': 33,
                      'above_60': 33,
                      }


def test_count_survived_first_class():
    pclass_filter = '1'
    answer = count_passengers(data, pclass_filter)

    assert answer == {'under_30': 0,
                      'above_60': 100,
                      }


def test_count_survived_third_class():
    pclass_filter = '3'
    answer = count_passengers(data, pclass_filter)

    assert answer == {'under_30': 50,
                      'above_60': 0,
                      }
