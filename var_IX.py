import csv
import streamlit as st
import matplotlib.pyplot as plt


def fetch_data():
    lines = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            lines.append(line)
    return lines


def count_prices(data, filter):
    ticket_prices = {'1': 0, '2': 0, '3': 0}
    if filter == 'муж.':
        filter = 'male'
    elif filter == 'жен.':
        filter = 'female'
    else:
        filter = None

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


def main():
    sex = st.selectbox('Пол пассажира', ['Любой', 'муж.', 'жен.'])
    data = count_prices(fetch_data(), filter=sex)

    st.dataframe(data, use_container_width=True)

    fig = plt.figure(figsize=(10, 5))
    p_class = data['Класс обслуживания']
    price = data['Цена билета']

    match sex:
        case 'муж.':
            color = 'blue'
        case 'жен.':
            color = 'pink'
        case 'Любой':
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
