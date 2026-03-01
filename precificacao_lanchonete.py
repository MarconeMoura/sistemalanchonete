import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lanchonete", layout="wide")
st.title("Sistema de Precificação e Lucro")

# Banco de dados temporário
if 'ingredientes' not in st.session_state:
    st.session_state.ingredientes = [
        {"nome": "Pão de Hambúrguer", "custo": 0.80},
        {"nome": "Carne (150g)", "custo": 4.50},
        {"nome": "Queijo (Fatia)", "custo": 0.60},
        {"nome": "Bacon (Fatia)", "custo": 0.90}
    ]

# Cadastro (Sprint 1)
with st.sidebar:
    st.header("Cadastro de Insumos")
    novo_nome = st.text_input("Novo Ingrediente")
    novo_custo = st.number_input("Custo (R$)", min_value=0.01)
    if st.button("Adicionar"):
        st.session_state.ingredientes.append({"nome": novo_nome, "custo": 
novo_custo})
        st.success("Adicionado!")

# Montar Lanche e Custo (Sprint 2)
st.subheader("Montar Ficha Técnica")
opcoes = [item['nome'] for item in st.session_state.ingredientes]
selecionados = st.multiselect("Selecione os ingredientes:", opcoes)

custo_total = sum([item['custo'] for item in st.session_state.ingredientes 
if item['nome'] in selecionados])
st.write(f"### Custo de Produção: R$ {custo_total:.2f}")

# Análise de Lucro (Sprint 3)
st.markdown("---")
st.subheader("Análise de Lucro")
preco_venda = st.number_input("Preço de Venda (R$)", min_value=0.0)

if preco_venda > 0 and custo_total > 0:
    lucro = preco_venda - custo_total
    margem = (lucro / preco_venda) * 100
    st.write(f"**Lucro Líquido:** R$ {lucro:.2f} (Margem: {margem:.1f}%)")
    if margem < 30:
        st.error("Cuidado: Margem muito baixa!")
