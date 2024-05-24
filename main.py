import streamlit as st
from var_IV import main as make_iv
from var_IX import main as make_ix
from  var_XVIII import main as make_xviii


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
    match var:
        case 4:
            make_iv()
        case 9:
            make_ix()
        case 18:
            make_xviii()


if __name__ == '__main__':
    main()
