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
        'under_30': round(data['under_30'] / data['all'] * 100),
        'above_60': round(data['above_60'] / data['all'] * 100)
    }


def make_iv(data):
    st.markdown(
        'Представлен вариант IV: Посчитать процент выживших молодых (до 30)'
        ' и старых (после 60) пассажиров, указав класс билета'
    )
    p_class = st.radio('Класс пассажира', ['Любой', '1', '2', '3'])
    survivors = count_passengers(data, p_class)
    st.dataframe(
        {
            'Возрастная группа': ['До 30 лет', 'Старше 60 лет'],
            'Доля спасшихся (%)': [
                survivors['under_30'],
                survivors['above_60']
            ]
        },
        use_container_width=True
    )
    fig = plt.figure(figsize=(10, 5))

    plt.bar(
        ['Доля выживших младше 30 лет', 'Доля выживших старше 60 лет'],
        [survivors['under_30'], survivors['above_60']],
        width=0.3
    )

    plt.xlabel('Возрастная группа')
    plt.ylabel('Доля выживших (%)')
    plt.title('Доля выживших пассажиров по возрастным группам')

    st.pyplot(fig)
