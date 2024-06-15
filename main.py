import streamlit as st
import csv
from var_IV import make_iv
from var_IX import make_ix
from var_XVIII import make_xviii


def make_page():
    st.title('Лабораторная работа №11')

    st.image('static/titanic.jpg')
    st.header('Данные пассажиров титаника')
    var = st.selectbox(
        'Выберите вариант', [4, 9, 18]
    )
    return var


def read_csv_data():
    data = []
    with open('data.csv') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            data.append(line)
    return data


def main():
    var = make_page()
    data = read_csv_data()
    match var:
        case 4:
            make_iv(data)
        case 9:
            make_ix(data)
        case 18:
            make_xviii(data)


if __name__ == '__main__':
    main()
