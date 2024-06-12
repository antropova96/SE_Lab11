import streamlit as st
import matplotlib.pyplot as plt


def count_passengers(csv_data, p_class) -> dict:
    data = {
        'under_30': 0,
        'above_60': 0,
        'all': 0
    }

    for line in csv_data:
        age = line[5]
        if age == '':
            continue  # отбрасываем строки
        age = float(age)

        if 30 < age < 60:
            continue

        if p_class != 'Любой':
            if line[2] != p_class:
                continue

        data['all'] += 1

        if int(line[1]) == 1:
            if age < 30.0:
                data['under_30'] += 1
            elif age > 60.0:
                data['above_60'] += 1

    return {
        'survival rate under 30': round(data['under_30'] / data['all'] * 100),
        'survival rate above 60': round(data['above_60'] / data['all'] * 100)
    }


def make_figure(data):
    fig = plt.figure(figsize=(10, 5))

    plt.bar(
        ['Доля выживших младше 30 лет', 'Доля выживших старше 60 лет'],
        [data['survival rate under 30'], data['survival rate above 60']],
    )

    plt.xlabel('Возрастная группа')
    plt.ylabel('Доля выживших (%)')
    plt.title('Доля выживших пассажиров по возрастным группам')

    st.pyplot(fig)


def make_iv(data):
    p_class = st.radio('Класс пассажира', ['Любой', '1', '2', '3'])
    survivors = count_passengers(data, p_class)
    st.table(
        {
            'Возрастная группа': ['До 30 лет', 'Старше 60 лет'],
            'Доля спасшихся (%)': [
                survivors['survival rate under 30'],
                survivors['survival rate above 60']
            ]
        }
    )
    make_figure(survivors)
