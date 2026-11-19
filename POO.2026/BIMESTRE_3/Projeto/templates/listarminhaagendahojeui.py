import streamlit as st
import pandas as pd
from service import Service
import time
from datetime import datetime

class ListarMinhaAgendaHojeUI:
    def main():
        st.header("Minha Agenda Hoje")
        tab1, tab2, = st.tabs(["Listar", "Atualizar"])
        with tab1: ListarMinhaAgendaHojeUI.listar()
        with tab2: ListarMinhaAgendaHojeUI.atualizar()
    
    def listar():
            horarios = Service.horario_listar()
            if len(horarios) == 0: st.write("Nenhum horário cadastrado hoje")
            else:
                dic = []
                for obj in horarios:
                    cliente = Service.cliente_listar_id(obj.get_id_cliente())
                    servico = Service.servico_listar_id(obj.get_id_servico())
                    profissional = Service.profissional_listar_id(obj.get_id_profissional())
                    horarios = Service.horario_listar(obj.get_data())
                    if cliente != None: cliente = cliente.get_nome()
                    if servico != None: servico = servico.get_descricao()
                    if profissional != None: profissional = profissional.get_nome()
                    dic.append({"id" : obj.get_id(), "data" : obj.get_data(),
                    "confirmado" : obj.get_confirmado(), "cliente" : cliente,
                    "serviço" : servico, "profissional" : profissional})
                df = pd.DataFrame(dic)
                st.dataframe(df)

    def atualizar():
            horarios = Service.horario_listar_confirmacao()
            if len(horarios) == 0: st.write("Nenhum horário confirmado")
            else:
                clientes = Service.cliente_listar()
                servicos = Service.servico_listar()
                profissionais = Service.profissional_listar()
                horarios = Service.horario_listar_confirmacao()
                op = st.selectbox("Atualização de Horários", horarios)
                data = st.text_input("Informe a nova data e horário do serviço", op.get_data().strftime("%d/%m/%Y %H:%M"))
                confirmado = st.checkbox("Nova confirmação", op.get_confirmado())
                id_cliente = None if op.get_id_cliente() in [0, None] else op.get_id_cliente()
                id_servico = None if op.get_id_servico() in [0, None] else op.get_id_servico()
                id_profissional = None if op.get_id_profissional() in [0, None] else op.get_id_profissional()
                cliente = st.selectbox("Informe o novo cliente", clientes, next((i for i, c in enumerate(clientes) if c.get_id() == id_cliente), None))
                servico = st.selectbox("Informe o novo serviço", servicos, next((i for i, s in enumerate(servicos) if s.get_id() == id_servico), None))
                profissional = st.selectbox("Informe o novo profissional", profissionais,\
                    next((i for i, s in enumerate(profissionais) if s.get_id() == id_profissional), None))
                if st.button("Atualizar"):
                    id_cliente = None
                    id_servico = None
                    id_profissional = None
                if cliente != None: id_cliente = cliente.get_id()
                if servico != None: id_servico = servico.get_id()
                if profissional != None: id_profissional = profissional.get_id()
                Service.horario_atualizar(op.get_id(), datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico, id_profissional)
                st.success("Horário atualizado com sucesso")
                time.sleep(2)
                st.rerun()