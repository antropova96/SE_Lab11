from var_IV import count_passengers, count_survival_rate

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

    assert answer == {'under_30': 1,
                      'above_60': 1,
                      'all': 3
                      }


def test_calculate_survival_rate():
    pclass_filter = 'Любой'
    suvivours = count_passengers(data, pclass_filter)

    survival_rate = count_survival_rate(suvivours)
    assert survival_rate == {
        'survival rate above 60': 33,
        'survival rate under 30': 33
    }


def test_count_survived_first_class():
    pclass_filter = 1
    answer = count_passengers(data, pclass_filter)

    assert answer == {'under_30': 0,
                      'above_60': 1,
                      'all': 1
                      }


def test_count_survived_third_class():
    pclass_filter = 3
    answer = count_passengers(data, pclass_filter)

    assert answer == {'under_30': 1,
                      'above_60': 0,
                      'all': 2
                      }


def test_count_survived_empty():
    answer = count_passengers([])

    assert list(answer.values()) == [0, 0, 0]
