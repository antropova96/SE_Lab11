import csv
import streamlit as st
import matplotlib.pyplot as plt


def parse_csv():
    result = []
    with open("data.csv") as file:
        csv_file = csv.reader(file)
        next(csv_file)
        for line in csv_file:
            result.append(line)
    return result


def count_survivors(filter, data):
    result = {
        'Пункт посадки': [],
        'Пассажиров': [],
        'Выживших': [],
    }
    for line in data:
        age_str = line[5]
        if age_str.isdigit():
            age = int(age_str)
        else:
            age = 0
        embarked = line[11]
        survived = int(line[1])
        if embarked:
            #  отбрасываем пассажиров старше указанного возраста
            if age > filter:
                continue
            if embarked in result['Пункт посадки']:
                indx = result['Пункт посадки'].index(embarked)
                result['Пассажиров'][indx] += 1
                if survived:
                    result['Выживших'][indx] += 1
            else:
                result['Пункт посадки'].append(embarked)
                result['Пассажиров'].append(1)
                result['Выживших'].append(1 if survived else 0)
    return result


def prepare_data(p_data):
    p_data['Доля выживших'] = []
    for v1, v2 in zip(
        p_data['Пассажиров'],
        p_data['Выживших']
    ):
        p_data['Доля выживших'].append(
            round(v2 / v1 * 100)
        )
    p_data.pop('Пассажиров')
    p_data.pop('Выживших')
    p_data['Пункт посадки'][p_data['Пункт посадки'].index('S')] = 'Саутгемптон'
    p_data['Пункт посадки'][p_data['Пункт посадки'].index('Q')] = 'Квинстаун'
    p_data['Пункт посадки'][p_data['Пункт посадки'].index('C')] = 'Шербур'
    return p_data


def main():
    st.markdown(
        'Представлен вариант IV: Посчитать долю выживших по каждому пункту '
        'посадки указав максимальный возраст'
    )
    slider = st.slider(
        'Укажите максимальный возраст',
        min_value=0,
        max_value=100,
        value=100
    )
    strings = parse_csv()
    data = prepare_data(count_survivors(slider, strings))
    st.table(data)

    fig = plt.figure(figsize=(10, 5))

    embarked = data['Пункт посадки']
    survival_rate = data['Доля выживших']

    plt.bar(embarked, survival_rate, width=0.3, label='Доля выживших')
    plt.xlabel('Место посадки')

    plt.ylabel('Доля выживших (%)')
    plt.title('Доля выживших пассажиров')
    plt.legend()

    st.pyplot(fig)
