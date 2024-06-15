import streamlit as st
import matplotlib.pyplot as plt


def count_prices(data, filter):
    ticket_prices = {'1': 0, '2': 0, '3': 0}
    for strings in data:
        pclass = strings[2]
        fare = float(strings[9])
        sex = strings[4]
        if filter:
            if sex == filter:
                ticket_prices[pclass] += fare
        else:
            ticket_prices[pclass] += fare

    return {
            'Класс обслуживания': list(ticket_prices.keys()),
            'Цена билета': list(ticket_prices.values()),
        }


def make_ix(data):
    st.markdown(
        'Представлен вариант IX: Найти количество пассажиров каждого пола по '
        'указанному классу обслуживания'
    )
    sex = st.selectbox('Пол пассажира', ['Любой', 'муж.', 'жен.'])
    if sex == 'муж.':
        sex = 'male'
    elif sex == 'жен.':
        sex = 'female'
    else:
        sex = None

    passengers = count_prices(data, filter=sex)

    st.dataframe(passengers, use_container_width=True)

    fig = plt.figure(figsize=(10, 5))
    p_class = passengers['Класс обслуживания']
    price = passengers['Цена билета']

    match sex:
        case 'male':
            color = 'blue'
        case 'female':
            color = 'pink'
        case _:
            color = 'green'

    plt.bar(
        p_class,
        price,
        width=0.3,
        label='Male',
        align='center',
        color=color
    )

    plt.title('Цены билетов по классам обслуживания')
    plt.xlabel('Класс обслуживания')
    plt.ylabel('Цена билета')

    st.pyplot(fig)
