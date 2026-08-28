import streamlit as st
from datetime import datetime, date
from paciente import Paciente

class PacienteUI:
    def main():
        st.header("Dados do Paciente")
        nome = st.text_input("Nome:")
        cpf = st.text_input("CPF:")
        telefone = st.text_input("Telefone:")
        nascimento = st.date_input("Data de nascimento", \
                                   min_value=date(1900, 1, 1), \
                                   max_value=date.today(), \
                                   format="DD/MM/YYYY")
        nascimento = datetime.combine(nascimento, datetime.min.time)
        if st.button("Idade"):
            x = Paciente(nome, cpf, telefone, nascimento)
            st.write(x.idade())
PacienteUI.main()