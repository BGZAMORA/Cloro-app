import streamlit as st

st.title("Calculadora de Cloro")

volumen = st.number_input("Ingrese el volumen actual de agua en litros:", min_value=0.0)

if st.button("Calcular"):
    cloro_necesario = volumen * 0.3
    st.success(f"Debe usar {cloro_necesario:.1f} ml de cloro para {volumen} litros de agua.")
