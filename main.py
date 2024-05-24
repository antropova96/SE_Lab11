import streamlit as st
from var_IV import main as make_iv


def make_page():
    st.title('Лабораторная работа №11')

    st.image('static/titanic.jpg')
    st.header('Данные пассажиров титаника')
    var = st.selectbox(
        'Выберите вариант', [4, 9, 18]
    )

    return var

def main():
    var = make_page()
    if var == 4:
        make_iv()


if __name__ == '__main__':
    main()
