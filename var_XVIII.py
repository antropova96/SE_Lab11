import streamlit as st
import matplotlib.pyplot as plt


def prepare_data(p_data):
    p_data['Доля выживших'] = []
    for v1, v2 in zip(
            p_data['Пассажиров'],
            p_data['Выживших']
    ):
        if v2 == 0:
            p_data['Доля выживших'].append(0)
        else:
            p_data['Доля выживших'].append(
                round(v2 / v1 * 100)
            )
    p_data.pop('Пассажиров')
    p_data.pop('Выживших')

    return p_data


def count_survivors(data, filter):
    result = {
        'Пункт посадки': ['Саутгемптон', 'Квинстаун', 'Шербур'],
        'Пассажиров': [0, 0, 0],
        'Выживших': [0, 0, 0],
    }
    for line in data:
        age_str = line[5]
        if age_str.isdigit():
            age = int(age_str)
        else:
            age = 0
        embarked = line[11]
        survived = line[1]
        if embarked:
            #  отбрасываем пассажиров старше указанного возраста
            if age > filter:
                continue
            match embarked:
                case 'S':
                    indx = 0
                case 'Q':
                    indx = 1
                case 'C':
                    indx = 2
            result['Пассажиров'][indx] += 1
            if survived == '1':
                result['Выживших'][indx] += 1
    return prepare_data(result)


def make_xviii(data):
    st.markdown(
        'Представлен вариант XVIII: Посчитать долю выживших по каждому пункту '
        'посадки указав максимальный возраст'
    )
    slider = st.slider(
        'Укажите максимальный возраст',
        min_value=0,
        max_value=100,
        value=100
    )
    data = count_survivors(data, filter=slider)
    st.dataframe(data, use_container_width=True)

    fig = plt.figure(figsize=(10, 5))

    embarked = data['Пункт посадки']
    survival_rate = data['Доля выживших']

    plt.bar(embarked, survival_rate, width=0.3, label='Доля выживших')
    plt.xlabel('Место посадки')

    plt.ylabel('Доля выживших (%)')
    plt.title('Доля выживших пассажиров')
    plt.legend()

    st.pyplot(fig)
